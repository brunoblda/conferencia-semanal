from pathlib import Path

import pandas as pd
import pdfplumber
from PIL import Image

from .layouts_pdf import LayoutPDF


class DiagnosticoReader:
    def __init__(self, path_diagnostico: Path):
        self.path_diagnostico = path_diagnostico

    def executar(self, pdf: pdfplumber.PDF, layout: LayoutPDF, dados: pd.DataFrame):

        limites_da_pagina = self._limites_da_pagina(pdf)

        imagens = self._layout_area(pdf, layout)

        debug_imagens = self._recorte_area(pdf, layout)

        self._exportar(layout, imagens, debug_imagens, limites_da_pagina, dados)

    def _limites_da_pagina(self, pdf) -> list:
        limites_da_pagina = []
        for pagina in pdf.pages:
            limites_da_pagina.append(pagina.bbox)
        return limites_da_pagina

    def _layout_area(self, pdf, layout):
        imagens = []
        for pagina in pdf.pages:
            imagem = pagina.to_image(resolution=144)
            imagem.draw_rect(
                layout.area, stroke="red", fill=(0, 0, 0, 0), stroke_width=2
            )
            imagens.append(imagem.annotated)
        return imagens

    def _recorte_area(self, pdf, layout):
        debug_imagens = []
        for pagina in pdf.pages:
            recorte = pagina.crop(layout.area)
            debug = recorte.to_image(resolution=144)
            debug.debug_tablefinder(layout.configuracao_tabela)
            debug_imagens.append(debug.annotated)
        return debug_imagens

    def _exportar(self, layout, imagens, debug_imagens, limites_da_pagina, dados):
        path_arquivo_layout = self.path_diagnostico / (
            "01-area-" + layout.tipo + ".png"
        )
        path_arquivo_recorte = self.path_diagnostico / (
            "02-recorte-" + layout.tipo + ".png"
        )
        path_arquivo_limites = self.path_diagnostico / (
            "03-limites-" + layout.tipo + ".txt"
        )
        path_arquivo_dados = self.path_diagnostico / (
            "04-dados-" + layout.tipo + ".csv"
        )

        self._salvar_imagens_empilhadas(imagens, path_arquivo_layout)
        self._salvar_imagens_empilhadas(debug_imagens, path_arquivo_recorte)
        self._salvar_txt(limites_da_pagina, path_arquivo_limites)
        self._salvar_dados_csv(dados, path_arquivo_dados)

    def _salvar_imagens_empilhadas(
        self, imagens: list[Image.Image], path_arquivo: Path
    ):
        if not imagens:
            return

        largura = max(imagem.width for imagem in imagens)
        altura_total = sum(imagem.height for imagem in imagens)
        imagem_final = Image.new("RGB", (largura, altura_total), "white")

        y_offset = 0

        path_arquivo.parent.mkdir(parents=True, exist_ok=True)

        for imagem in imagens:
            imagem_final.paste(imagem, (0, y_offset))
            y_offset += imagem.height
        imagem_final.save(path_arquivo)

    def _salvar_txt(self, conteudo: list, path_arquivo: Path):
        conteudo = "\n".join(str(limite) for limite in conteudo)
        path_arquivo.parent.mkdir(parents=True, exist_ok=True)
        with open(path_arquivo, "w", encoding="utf-8") as f:
            f.write(conteudo)

    def _salvar_dados_csv(self, dados: pd.DataFrame, path_arquivo: Path):
        path_arquivo.parent.mkdir(parents=True, exist_ok=True)
        dados.to_csv(path_arquivo, index=False, encoding="utf-8")

import os
from pathlib import Path

import pandas as pd
import pdfplumber

from .diagnostico_reader import DiagnosticoReader
from .layouts_pdf import LayoutPDF


class LeitorPDF:
    def __init__(self, diagnostico: DiagnosticoReader, diagnosticar: bool = False):
        self.diagnostico = diagnostico
        self.diagnosticar = diagnosticar

    def _validar_arquivo(self, path_entrada: Path):
        self._validar_arquivo_existe(path_entrada)
        self._validar_extensao_arquivo(path_entrada)

    def _validar_arquivo_existe(self, path_entrada: Path):
        if not os.path.exists(path_entrada):
            raise FileNotFoundError(f"O arquivo {path_entrada} não existe.")

    def _validar_extensao_arquivo(self, path_entrada: Path):
        if not str(path_entrada).lower().endswith(".pdf"):
            raise ValueError(f"O arquivo {path_entrada} não é um arquivo PDF.")

    def ler(self, path_entrada: Path, layout: LayoutPDF) -> pd.DataFrame:
        self._validar_arquivo(path_entrada)
        area = layout.area
        configuracao = layout.configuracao_tabela
        tabelas = []
        with pdfplumber.open(path_entrada) as pdf:
            for pagina in pdf.pages:
                recorte = pagina.crop(area)

                # Adiciona as tabelas extraídas do recorte à lista de tabelas.
                tabelas.extend(recorte.extract_tables(table_settings=configuracao))

            tabelas = [pd.DataFrame(tabela) for tabela in tabelas if tabela]

            dados = pd.concat(tabelas, ignore_index=True) if tabelas else pd.DataFrame()

            if self.diagnosticar:
                self.diagnostico.executar(pdf, layout, dados)

        return dados

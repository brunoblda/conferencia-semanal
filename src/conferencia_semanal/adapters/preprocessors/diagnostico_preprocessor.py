from pathlib import Path

import pandas as pd

from conferencia_semanal.application.dto.tipo_tabela import TipoTabela


class DiagnosticoPreprocessor:
    def __init__(self, path_diagnostico: Path) -> None:
        self.path_diagnostico = path_diagnostico

    def execute(self, dados: pd.DataFrame, tipo_tabela: TipoTabela) -> None:
        path_arquivo = self.path_diagnostico / f"dados-preprocessados-{tipo_tabela}.csv"
        path_arquivo.parent.mkdir(parents=True, exist_ok=True)
        dados.to_csv(path_arquivo, index=False)

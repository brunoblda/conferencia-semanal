from decimal import Decimal, InvalidOperation

import pandas as pd

from conferencia_semanal.adapters.preprocessors.diagnostico_preprocessor import (
    DiagnosticoPreprocessor,
)
from conferencia_semanal.application.dto.tipo_tabela import TipoTabela


class DadosPreprocessor:
    def __init__(
        self, diagnostico: DiagnosticoPreprocessor, diagnosticar: bool = False
    ):
        self.diagnostico = diagnostico
        self.diagnosticar = diagnosticar

    def execute(self, tabela: pd.DataFrame, tipo_tabela: TipoTabela) -> pd.DataFrame:
        metodos = {
            TipoTabela.PLANO_INTERNO: self._preprocess_pi,
            TipoTabela.SEOF: self._preprocess_pi_seof,
            TipoTabela.SIAFI: self._preprocess_pi_siafi,
            TipoTabela.PLANO_INTERNO_RESERVA: self._preprocess_pi_reserva,
            TipoTabela.SEOF_RESERVA: self._preprocess_pi_seof_reserva,
            TipoTabela.SIAFI_RESERVA: self._preprocess_pi_siafi_reserva,
        }
        metodo = metodos.get(tipo_tabela)
        if metodo is None:
            raise ValueError(f"Tipo de tabela não suportado: {tipo_tabela}")

        tabela_preprocessada = metodo(tabela)

        if self.diagnosticar:
            self.diagnostico.execute(tabela_preprocessada, tipo_tabela)

        return tabela_preprocessada

    def _preprocess_pi(self, tabela: pd.DataFrame) -> pd.DataFrame:
        coluna_monetaria = 2
        tabela[coluna_monetaria] = tabela[coluna_monetaria].map(
            self._transforma_texto_em_decimal
        )
        tabela[coluna_monetaria] = tabela[coluna_monetaria].map(
            self._transforma_traco_em_zero
        )

        return tabela

    def _preprocess_pi_seof(self, tabela: pd.DataFrame) -> pd.DataFrame:
        coluna_monetaria = 1
        tabela[coluna_monetaria] = tabela[coluna_monetaria].map(
            self._transforma_texto_em_decimal
        )

        return tabela

    def _preprocess_pi_siafi(self, tabela: pd.DataFrame) -> pd.DataFrame:
        coluna_ptres = 0
        coluna_natureza_de_despesa = 2
        coluna_monetaria = 3
        tabela[coluna_ptres] = tabela[coluna_ptres].map(
            self._transforma_numero_em_texto
        )
        tabela[coluna_natureza_de_despesa] = tabela[coluna_natureza_de_despesa].map(
            self._transforma_numero_em_texto
        )
        tabela[coluna_monetaria] = tabela[coluna_monetaria].map(
            self._transforma_texto_em_decimal
        )

        return tabela

    def _preprocess_pi_reserva(self, tabela: pd.DataFrame) -> pd.DataFrame:
        coluna_monetaria = 1
        tabela[coluna_monetaria] = tabela[coluna_monetaria].map(
            self._transforma_texto_em_decimal
        )
        tabela[coluna_monetaria] = tabela[coluna_monetaria].map(
            self._transforma_traco_em_zero
        )

        return tabela

    def _preprocess_pi_seof_reserva(self, tabela: pd.DataFrame) -> pd.DataFrame:
        coluna_monetaria = 1
        tabela[coluna_monetaria] = tabela[coluna_monetaria].map(
            self._transforma_texto_em_decimal
        )

        return tabela

    def _preprocess_pi_siafi_reserva(self, tabela: pd.DataFrame) -> pd.DataFrame:
        coluna_ptres = 0
        coluna_natureza_de_despesa = 2
        coluna_monetaria = 3
        tabela[coluna_ptres] = tabela[coluna_ptres].map(
            self._transforma_numero_em_texto
        )
        tabela[coluna_natureza_de_despesa] = tabela[coluna_natureza_de_despesa].map(
            self._transforma_numero_em_texto
        )
        tabela[coluna_monetaria] = tabela[coluna_monetaria].map(
            self._transforma_texto_em_decimal
        )

        return tabela

    @staticmethod
    def _transforma_texto_em_decimal(celula: object) -> object | Decimal:
        if isinstance(celula, str):
            celula_formatada = (
                celula.replace(" ", "").replace(".", "").replace(",", ".").strip()
            )
            try:
                decimal_celula = Decimal(celula_formatada)
                return decimal_celula
            except InvalidOperation:
                return celula
        return celula

    @staticmethod
    def _transforma_traco_em_zero(celula: object) -> object | Decimal:
        if isinstance(celula, str) and celula.strip() == "-":
            return Decimal("0")
        return celula

    @staticmethod
    def _transforma_numero_em_texto(celula: object) -> object | str:
        if pd.isna(celula):
            return celula
        if isinstance(celula, (int, float, Decimal)):
            return str(int(celula))
        return celula

from pathlib import Path

from conferencia_semanal.adapters.preprocessors.dados_preprocessor import (
    DadosPreprocessor,
)
from conferencia_semanal.adapters.preprocessors.diagnostico_preprocessor import (
    DiagnosticoPreprocessor,
)
from conferencia_semanal.infrastructure.pdf.readers.diagnostico_reader import (
    DiagnosticoReader,
)
from conferencia_semanal.infrastructure.pdf.readers.layouts_pdf import (
    LAYOUT_PLANO_INTERNO,
    LAYOUT_PLANO_INTERNO_RESERVA,
    LAYOUT_SEOF,
    LAYOUT_SEOF_RESERVA,
    LAYOUT_SIAFI,
    LAYOUT_SIAFI_RESERVA,
)
from conferencia_semanal.infrastructure.pdf.readers.leitor_pdf import LeitorPDF


def processar_pdf(
    path_pdf: Path,
    leitor: LeitorPDF,
    layout,
):
    dados = leitor.ler(path_pdf, layout)

    return dados


def main() -> None:

    print("Hello from conferencia-semanal!")

    path_entrada_pdf = Path("tests/dados/2026-08-29/")
    path_diagnostico_reader = Path("diagnostico/reader/")
    path_diagnostico_preprocessor = Path("diagnostico/preprocessor/")
    diagnosticar = True

    pi_pdf = "pi.pdf"

    pi_seof_pdf = "pi_seof.pdf"

    pi_siafi_pdf = "pi_siafi.pdf"

    pi_reserva_pdf = "pi_reserva.pdf"

    pi_seof_reserva_pdf = "pi_seof_reserva.pdf"

    pi_siafi_reserva_pdf = "pi_siafi_reserva.pdf"

    path_pi_pdf = path_entrada_pdf / pi_pdf

    path_pi_seof_pdf = path_entrada_pdf / pi_seof_pdf

    path_pi_siafi_pdf = path_entrada_pdf / pi_siafi_pdf

    path_pi_reserva_pdf = path_entrada_pdf / pi_reserva_pdf

    path_pi_seof_reserva_pdf = path_entrada_pdf / pi_seof_reserva_pdf

    path_pi_siafi_reserva_pdf = path_entrada_pdf / pi_siafi_reserva_pdf

    diagnostico_reader = DiagnosticoReader(path_diagnostico_reader)

    leitor = LeitorPDF(diagnostico_reader, diagnosticar)

    dados_pi = processar_pdf(path_pi_pdf, leitor, LAYOUT_PLANO_INTERNO)
    dados_pi_seof = processar_pdf(path_pi_seof_pdf, leitor, LAYOUT_SEOF)
    dados_pi_siafi = processar_pdf(path_pi_siafi_pdf, leitor, LAYOUT_SIAFI)
    dados_pi_reserva = processar_pdf(
        path_pi_reserva_pdf,
        leitor,
        LAYOUT_PLANO_INTERNO_RESERVA,
    )
    dados_pi_seof_reserva = processar_pdf(
        path_pi_seof_reserva_pdf,
        leitor,
        LAYOUT_SEOF_RESERVA,
    )
    dados_pi_siafi_reserva = processar_pdf(
        path_pi_siafi_reserva_pdf,
        leitor,
        LAYOUT_SIAFI_RESERVA,
    )

    diagnostico_preprocessor = DiagnosticoPreprocessor(path_diagnostico_preprocessor)

    dados_pi_preprocessado = DadosPreprocessor(
        diagnostico_preprocessor, diagnosticar
    ).execute(dados_pi, LAYOUT_PLANO_INTERNO.tipo)
    dados_pi_seof_preprocessado = DadosPreprocessor(
        diagnostico_preprocessor, diagnosticar
    ).execute(dados_pi_seof, LAYOUT_SEOF.tipo)
    dados_pi_siafi_preprocessado = DadosPreprocessor(
        diagnostico_preprocessor, diagnosticar
    ).execute(dados_pi_siafi, LAYOUT_SIAFI.tipo)
    dados_pi_reserva_preprocessado = DadosPreprocessor(
        diagnostico_preprocessor, diagnosticar
    ).execute(dados_pi_reserva, LAYOUT_PLANO_INTERNO_RESERVA.tipo)
    dados_pi_seof_reserva_preprocessado = DadosPreprocessor(
        diagnostico_preprocessor, diagnosticar
    ).execute(dados_pi_seof_reserva, LAYOUT_SEOF_RESERVA.tipo)
    dados_pi_siafi_reserva_preprocessado = DadosPreprocessor(
        diagnostico_preprocessor, diagnosticar
    ).execute(dados_pi_siafi_reserva, LAYOUT_SIAFI_RESERVA.tipo)

    dados_pi_preprocessado.head()
    dados_pi_seof_preprocessado.head()
    dados_pi_siafi_preprocessado.head()
    dados_pi_reserva_preprocessado.head()
    dados_pi_seof_reserva_preprocessado.head()
    dados_pi_siafi_reserva_preprocessado.head()


if __name__ == "__main__":
    main()

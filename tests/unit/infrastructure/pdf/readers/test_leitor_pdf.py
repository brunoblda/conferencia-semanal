import pytest

from conferencia_semanal.infrastructure.pdf.readers.diagnostico_reader import (
    DiagnosticoReader,
)
from conferencia_semanal.infrastructure.pdf.readers.layouts_pdf import (
    LAYOUT_PLANO_INTERNO,
)
from conferencia_semanal.infrastructure.pdf.readers.leitor_pdf import LeitorPDF


def test_lanca_erro_quando_arquivo_inexistente(tmp_path):
    caminho_inexistente = tmp_path / "ausente.pdf"
    leitor = LeitorPDF(DiagnosticoReader(tmp_path))

    with pytest.raises(FileNotFoundError, match="não existe"):
        leitor.ler(caminho_inexistente, LAYOUT_PLANO_INTERNO)


def test_lanca_erro_quando_arquivo_nao_e_pdf(tmp_path):
    caminho_nao_pdf = tmp_path / "arquivo.txt"
    caminho_nao_pdf.touch()

    leitor = LeitorPDF(DiagnosticoReader(tmp_path))

    with pytest.raises(ValueError, match="não é um arquivo PDF"):
        leitor.ler(caminho_nao_pdf, LAYOUT_PLANO_INTERNO)

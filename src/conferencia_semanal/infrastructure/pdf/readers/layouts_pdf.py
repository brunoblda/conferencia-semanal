from dataclasses import dataclass

from conferencia_semanal.application.dto.tipo_tabela import TipoTabela


@dataclass
class LayoutPDF:
    tipo: str
    area: tuple[int, int, int, int]
    configuracao_tabela: dict


# explicit vertical lines = [x0, top, x1, bottom]

LAYOUT_PLANO_INTERNO = LayoutPDF(
    tipo=TipoTabela.PLANO_INTERNO,
    area=(120, 105, 475, 795),
    configuracao_tabela={
        "vertical_strategy": "explicit",
        "explicit_vertical_lines": [125, 325, 400, 470],
        "horizontal_strategy": "text",
        "intersection_tolerance": 20,
    },
)

LAYOUT_SEOF = LayoutPDF(
    tipo=TipoTabela.SEOF,
    area=(35, 155, 560, 725),
    configuracao_tabela={
        "vertical_strategy": "lines",
        "horizontal_strategy": "text",
        "intersection_tolerance": 10,
    },
)

LAYOUT_SIAFI = LayoutPDF(
    tipo=TipoTabela.SIAFI,
    area=(510, 130, 755, 520),
    configuracao_tabela={
        "vertical_strategy": "lines",
        "horizontal_strategy": "lines",
    },
)

LAYOUT_PLANO_INTERNO_RESERVA = LayoutPDF(
    tipo=TipoTabela.PLANO_INTERNO_RESERVA,
    area=(125, 85, 470, 780),
    configuracao_tabela={
        "vertical_strategy": "explicit",
        "explicit_vertical_lines": [130, 400, 465],
        "horizontal_strategy": "text",
        "intersection_tolerance": 10,
    },
)

LAYOUT_SEOF_RESERVA = LayoutPDF(
    tipo=TipoTabela.SEOF_RESERVA,
    area=(35, 155, 560, 725),
    configuracao_tabela={
        "vertical_strategy": "lines",
        "horizontal_strategy": "text",
        "intersection_tolerance": 10,
    },
)

LAYOUT_SIAFI_RESERVA = LayoutPDF(
    tipo=TipoTabela.SIAFI_RESERVA,
    area=(510, 115, 705, 535),
    configuracao_tabela={
        "vertical_strategy": "lines",
        "horizontal_strategy": "lines",
    },
)

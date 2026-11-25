from enum import StrEnum


class TipoTabela(StrEnum):
    PLANO_INTERNO = "plano_interno"
    SEOF = "seof"
    SIAFI = "siafi"
    PLANO_INTERNO_RESERVA = "plano_interno_reserva"
    SEOF_RESERVA = "seof_reserva"
    SIAFI_RESERVA = "siafi_reserva"

import pandas as pd


class PIClassifier:
    def __init__(self):
        pass

    def classify(self, data: pd.DataFrame):
        """
        acao_pattern = r"^[0-9]{2}\\.[0-9]{3}\\.[0-9]{4}\\.[A-Z0-9]{4}\\.[0-9]{2}"
        PO_pattern = r"^PO [0-9]{4}"
        PTRES_pattern = r"[0-9]{6}"
        pi_pattern = r"^(?=.{1,11} - )([A-Z0-9]+(?:[- ][A-Z0-9]+)*) - "
        elemento_pattern = r"[0-9]\\.[0-9]\\.[0-9]{2}\\.[0-9]{2}\\.00"
        item_pattern = r"[0-9]{2}\\.[0-9]{2}\\.[0-9]{2}"
        """

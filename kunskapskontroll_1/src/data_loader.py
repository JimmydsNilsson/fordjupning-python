import pandas as pd
from logger import setup_logger

# Skapar logger för denna modul
logger = setup_logger()

# Läser in en CSV-fil och returnerar en DataFrame
def load_csv(path: str):
    try:
        df = pd.read_csv(path)
        logger.info(f"Läste in CSV med {len(df)} rader")
        return df
    except Exception as e:
        logger.error(f"Kunde inte läsa CSV: {e}")
        raise

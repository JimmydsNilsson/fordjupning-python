import os
from kunskapskontroll_1.src.data_loader import load_csv
from kunskapskontroll_1.src.database import init_db, insert_data
from kunskapskontroll_1.src.logger import setup_logger
from datetime import datetime

# Skapar logger för huvudprogrammet
logger = setup_logger()

# Hittar projektets rotmapp automatiskt
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Bygger en absolut sökväg till CSV-filen
CSV_PATH = os.path.join(BASE_DIR, "data", "input.csv")

# Kör hela ETL-flödet
def run():
    logger.info("Startar ETL-processen")

    # Läser in CSV-filen via absolut sökväg
    df = load_csv(CSV_PATH)

    # Byter kolumnnamn så de matchar databasens struktur
    df = df.rename(columns={
        "city": "name",
        "temperature": "value"
    })

    # Lägger till en timestamp-kolumn
    df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Skapar databas och tabell om de inte finns
    init_db()

    # Lägger in datan i databasen
    insert_data(df)

    logger.info("ETL-processen är klar")

# Körs bara om filen körs direkt
if __name__ == "__main__":
    run()

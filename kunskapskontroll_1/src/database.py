import sqlite3
from logger import setup_logger

# Skapar logger för denna modul
logger = setup_logger()

# Skapar databasen och tabellen om de inte redan finns
def init_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            value REAL,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()
    logger.info("Databas och tabell är redo")

# Lägger in rader från en DataFrame i databasen
def insert_data(df):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO my_table (name, value, timestamp)
            VALUES (?, ?, ?)
        """, (row["name"], row["value"], row["timestamp"]))

    conn.commit()
    conn.close()
    logger.info("Data har lagts in i databasen")

import pandas as pd
import os

def process_strava(df: pd.DataFrame) -> pd.DataFrame:
    # Exempel: filtrera bort orimliga värden
    df = df.dropna(subset=["distance_km", "duration_min"])
    df = df[df["distance_km"] > 0]
    df = df[df["duration_min"] > 0]

    # Beräkna tempo (min/km)
    df["pace_min_per_km"] = df["duration_min"] / df["distance_km"]

    # Veckonummer
    df["year_week"] = df["date"].dt.strftime("%Y-%U")

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/strava_processed.csv", index=False)
    return df

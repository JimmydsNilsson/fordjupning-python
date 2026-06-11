import pandas as pd

def weekly_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("year_week")
        .agg(
            total_distance_km=("distance_km", "sum"),
            total_duration_min=("duration_min", "sum"),
            avg_pace_min_per_km=("pace_min_per_km", "mean"),
        )
        .reset_index()
    )
    return summary

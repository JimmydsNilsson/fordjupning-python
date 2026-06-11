from load_data import load_strava_data
from process_strava import process_strava
from analyze_strava import weekly_summary

# Importera alla visualiseringar
from visualize_strava import (
    plot_weekly_distance,
    plot_pace_over_time,
    plot_heart_rate_vs_distance,
    plot_sport_distribution,
    plot_correlation_heatmap
)

def main():
    # 1. Läs in rådata
    df = load_strava_data("data/raw/strava_activities.csv")

    # 2. Processa data
    df_processed = process_strava(df)

    # 3. Analys
    summary = weekly_summary(df_processed)

    # --- UTSKRIFTER I TERMINALEN ---
    print("\n--- Veckosammanfattning (första 10 rader) ---")
    print(summary.head(10))

    print("\n--- Grundläggande statistik ---")
    print(df_processed.describe())

    print("\n--- Antal pass per sporttyp ---")
    print(df_processed["sport"].value_counts())

    print("\n--- Korrelationer ---")
    print(df_processed[["distance_km", "duration_min", "avg_heart_rate", "elevation_gain"]].corr())

    # 4. Visualiseringar
    plot_weekly_distance(summary)
    plot_pace_over_time(df_processed)
    plot_heart_rate_vs_distance(df_processed)
    plot_sport_distribution(df_processed)
    plot_correlation_heatmap(df_processed)

    print("\nKlar! Kolla data/processed och reports/figures för grafer och bearbetad data.")

if __name__ == "__main__":
    main()

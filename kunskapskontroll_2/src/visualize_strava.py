import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Skapa mapp om den saknas
os.makedirs("reports/figures", exist_ok=True)

def plot_weekly_distance(summary: pd.DataFrame):
    plt.figure(figsize=(10, 5))
    plt.plot(summary["year_week"], summary["total_distance_km"], marker="o")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Total distans (km)")
    plt.title("Veckovis total distans")
    plt.tight_layout()
    plt.savefig("reports/figures/weekly_distance.png")
    plt.close()

def plot_pace_over_time(df: pd.DataFrame):
    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["pace_min_per_km"], marker="o", alpha=0.7)
    plt.title("Tempo över tid (min/km)")
    plt.ylabel("Tempo (min/km)")
    plt.xlabel("Datum")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("reports/figures/pace_over_time.png")
    plt.close()

def plot_heart_rate_vs_distance(df: pd.DataFrame):
    plt.figure(figsize=(8, 5))
    plt.scatter(df["distance_km"], df["avg_heart_rate"], alpha=0.7)
    plt.title("Puls vs distans")
    plt.xlabel("Distans (km)")
    plt.ylabel("Puls (bpm)")
    plt.tight_layout()
    plt.savefig("reports/figures/hr_vs_distance.png")
    plt.close()

def plot_sport_distribution(df: pd.DataFrame):
    plt.figure(figsize=(6, 6))
    df["sport"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Fördelning av sporttyper")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("reports/figures/sport_distribution.png")
    plt.close()

def plot_correlation_heatmap(df: pd.DataFrame):
    plt.figure(figsize=(8, 6))
    corr = df[["distance_km", "duration_min", "avg_heart_rate", "elevation_gain"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Korrelationer mellan variabler")
    plt.tight_layout()
    plt.savefig("reports/figures/correlation_heatmap.png")
    plt.close()

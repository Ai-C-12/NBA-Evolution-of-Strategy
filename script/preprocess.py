# src/preprocess.py
# Preprocess and merge advanced + basic NBA data

import pandas as pd
import argparse
import os

# Argument setup
parser = argparse.ArgumentParser(description="Preprocess NBA stats data")
parser.add_argument("--input", default="data/raw", help="Folder containing raw CSV files")
parser.add_argument("--output", default="data/processed/nba_processed_data.csv", help="Path to save merged data")
args = parser.parse_args()

# File paths
advanced_path = os.path.join(args.input, "advanced_NBA_data.csv")
basic_path = os.path.join(args.input, "basic_NBA_data.csv")

print("Loading raw data...")
final_data1 = pd.read_csv(advanced_path)
final_data2 = pd.read_csv(basic_path)

# Merge datasets
print("Merging advanced and basic stats...")
final_df = pd.merge(
    final_data1,
    final_data2,
    on=["TEAM_NAME", "SEASON", "GP", "W", "L", "W_PCT"],
    how="outer"
)

# Cleaning steps
print("Cleaning data...")
final_df.dropna(subset=["TEAM_NAME"], inplace=True)

# Fill missing basic stats with 0
basic_stats = [
    "FGM", "FGA", "FG3M", "FG3A", "FTM", "FTA",
    "OREB", "DREB", "REB", "AST", "TOV", "STL",
    "BLK", "BLKA", "PF", "PFD", "PTS"
]
final_df[basic_stats] = final_df[basic_stats].fillna(0)

# Reset index
final_df.reset_index(drop=True, inplace=True)

# Save processed file
os.makedirs(os.path.dirname(args.output), exist_ok=True)
final_df.to_csv(args.output, index=False)
print(f"Preprocessing complete! Saved merged data to {args.output}")

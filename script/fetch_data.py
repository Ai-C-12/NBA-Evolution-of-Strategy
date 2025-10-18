import time
import pandas as pd
import os
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.static import teams

# --- Setup ---
RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

# Get official NBA team IDs (franchises only)
nba_team_ids = [team["id"] for team in teams.get_teams()]

# --- Function to fetch team stats for a given season ---
def fetch_season_stats(season, measure_type="Base"):
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season=season,
        measure_type_detailed_defense=measure_type
    )
    df = stats.get_data_frames()[0]

    # Keep only NBA franchises
    df = df[df["TEAM_ID"].isin(nba_team_ids)]
    df["SEASON"] = season
    return df

# Build list of seasons
seasons = [f"{year}-{str(year + 1)[-2:]}" for year in range(2000, 2025)]

# --- Fetch Advanced Data ---
print("Fetching advanced NBA data...")
advanced_data = []
for season in seasons:
    advanced_data.append(fetch_season_stats(season, measure_type="Advanced"))
    time.sleep(0.6)  # Respect API rate limits

final_advanced = pd.concat(advanced_data, ignore_index=True)
final_advanced = final_advanced.drop(
    [
        "TEAM_ID", "MIN", "E_OFF_RATING", "E_DEF_RATING", "E_NET_RATING",
        "E_PACE", "PACE_PER40", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK",
        "MIN_RANK", "OFF_RATING_RANK", "DEF_RATING_RANK", "NET_RATING_RANK",
        "AST_PCT_RANK", "AST_TO_RANK", "AST_RATIO_RANK", "OREB_PCT_RANK",
        "DREB_PCT_RANK", "REB_PCT_RANK", "TM_TOV_PCT_RANK", "EFG_PCT_RANK",
        "TS_PCT_RANK", "PACE_RANK", "PIE_RANK"
    ],
    axis=1
)
final_advanced.to_csv(os.path.join(RAW_DIR, "advanced_NBA_data.csv"), index=False)
print("Advanced data saved.")

# --- Fetch Basic Data ---
print("\nFetching basic NBA data...")
basic_data = []
for season in seasons:
    basic_data.append(fetch_season_stats(season, measure_type="Base"))
    time.sleep(0.6)

final_basic = pd.concat(basic_data, ignore_index=True)
final_basic = final_basic.drop(
    [
        "TEAM_ID", "MIN", "GP_RANK", "MIN_RANK", "W_RANK", 
        "L_RANK", "W_PCT_RANK", "FGM_RANK", "FGA_RANK", 
        "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", 
        "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", 
        "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", 
        "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", 
        "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK"
    ],
    axis=1
)
final_basic.to_csv(os.path.join(RAW_DIR, "basic_NBA_data.csv"), index=False)
print("Basic data saved.")

print("\nFetch complete! Files saved to data/raw/")
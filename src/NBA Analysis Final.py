"""
NBA Strategy Evolution Analysis
- Fetches NBA team stats (2000–2025) via nba_api
- Saves cleaned advanced and basic datasets
- Generates strategy-focused visualizations:
    * Pace & Possessions
    * Rebounding strategy
    * Defense trends
    * Shooting efficiency (eFG% & TS%)
    * Assisted vs Isolation baskets
    * 3-Point evolution
- Outputs all figures as PNGs in /outputs/
"""
import time
import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.static import teams
import matplotlib.pyplot as plt


# Get official NBA team IDs (franchises only)
nba_team_ids = [team["id"] for team in teams.get_teams()]

# Function to fetch team stats for a given season
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
seasons = [f"{year}-{str(year+1)[-2:]}" for year in range(2000, 2025)]


# -------- Fetch Advanced Data --------
advanced_data = []
for season in seasons:
    advanced_data.append(fetch_season_stats(season, measure_type="Advanced"))
    time.sleep(0.6)  # API rate limit

final_advanced = pd.concat(advanced_data, ignore_index=True)
final_advanced = final_advanced.drop(
    ["TEAM_ID", "MIN", "E_OFF_RATING", "E_DEF_RATING", "E_NET_RATING", 
     "E_PACE", "PACE_PER40", "GP_RANK"], axis=1
)
final_advanced.to_csv("finalized_NBA_data.csv", index=False)


# -------- Fetch Basic Data --------
basic_data = []
for season in seasons:
    basic_data.append(fetch_season_stats(season, measure_type="Base"))
    time.sleep(0.6)

final_basic = pd.concat(basic_data, ignore_index=True)
final_basic = final_basic.drop(["TEAM_ID", "MIN", "GP_RANK", "MIN_RANK"], axis=1)
final_basic.to_csv("basic_NBA_data.csv", index=False)


final_data1 = pd.read_csv("finalized_NBA_data.csv")
final_data2 = pd.read_csv("basic_NBA_data.csv")
final_df = pd.concat([final_data1, final_data2])


# -----------------------
# PACE ANALYSIS
# -----------------------
fig, ax1 = plt.subplots(figsize=(12,6))

ax2 = ax1.twinx() 

Pace = final_df.groupby("SEASON")[["PACE", "POSS"]].mean()
ax1.plot(Pace.index, Pace["PACE"], color="blue", marker="o", label="Pace")
ax2.plot(Pace.index, Pace["POSS"], color="red", marker="s", label="Possessions")

ax1.set_xlabel("Seasons")
ax1.set_ylabel("Pace (Possessions per 48 min)", color="blue")
ax2.set_ylabel("Possessions (Raw)", color="red")

plt.title("NBA Pace vs Possessions Over the Years")
ax1.set_xticks(Pace.index[::2])
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
plt.show()


# -----------------------
# REBOUNDS ANALYSIS
# -----------------------
Reb = final_df.groupby("SEASON")[["OREB_PCT", "DREB_PCT"]].mean() * 100
Reb5 = Reb.iloc[::4]

ax = Reb5.plot(kind="bar", figsize=(12,6))
plt.title("Rebounding Strategy (Every 5 Seasons)")
plt.ylabel("Rebound %")
plt.xlabel("Season")
plt.legend(["Offensive Rebounding %", "Defensive Rebounding %"])
ax.set_yticks(range(0, 71, 10))
ax.set_yticklabels([f"{i}%" for i in range(0, 71, 10)])
plt.xticks(rotation=45)
plt.show()


# -----------------------
# DEFENSE ANALYSIS
# -----------------------
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Top plot: Defensive Rating
DefRating = final_df.groupby("SEASON")[["DEF_RATING"]].mean()
ax1.plot(DefRating.index, DefRating["DEF_RATING"], color="blue", marker="o", label="Defensive Rating")
ax1.set_ylabel("Defensive Rating (Pts per 100 possessions)")
ax1.set_title("Defense Over the Years")
ax1.legend(loc="upper right")

# Bottom plot: Blocks & Steals
Def = final_df.groupby("SEASON")[["BLK", "STL"]].mean()
ax2.plot(Def.index, Def["BLK"], color="green", marker="s", label="Blocks")
ax2.plot(Def.index, Def["STL"], color="red", marker="^", label="Steals")
ax2.set_ylabel("Per Game")
ax2.set_xlabel("Seasons")
ax2.legend(loc="upper right")

ax2.set_xticks(Def.index[::2])  

plt.tight_layout()
plt.show()


# --------------------------------------------
# EFFECTIVE FG & TRUE SHOOTING ANALYSIS
# --------------------------------------------
fig, ax1 = plt.subplots(figsize=(12,6))

Shooting = final_df.groupby("SEASON")[["EFG_PCT", "TS_PCT", "FGA"]].mean()
Shooting[["EFG_PCT", "TS_PCT"]] *= 100
ax1.plot(Shooting.index, Shooting["EFG_PCT"], color="blue", marker="o", label="Effective Field Goals")
ax1.plot(Shooting.index, Shooting["TS_PCT"], color="red", marker="o", label="True Shooting")
ax1.set_ylabel("Shooting Efficiency (%)")

ax2 = ax1.twinx()
ax2.scatter(Shooting.index, Shooting["FGA"], marker="*", color="green", label="Field Goals Attempted")
ax2.set_ylabel("Field Goal Attempts")

ax1.set_xticks(Shooting.index[::2])
ax1.set_yticks(range(48, 59, 2))
ax1.set_yticklabels([f"{i}%" for i in range(48, 59, 2)])
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
plt.title("Scoring Efficiency")
ax1.set_xlabel("Seasons")
plt.show()


# ------------------------------------
# ASSISTS AND ISOLATION ANALYSIS
# ------------------------------------
fig, ax1 = plt.subplots(figsize=(12,6))

Assist = final_df.groupby("SEASON")[["AST", "FGM"]].sum()
assistPct = (Assist["AST"] / Assist["FGM"]) * 100

ISO = final_df.groupby("SEASON")[["AST", "FGM"]].sum()
isoPct = ((ISO["FGM"] - ISO["AST"]) / ISO["FGM"]) * 100

ax1.plot(Assist.index, assistPct, marker="o", color="red", label="Assist Percentage")
ax1.plot(ISO.index, isoPct, marker="o", color="green", label="Percentage of ISO baskets")
ax1.set_yticks(range(40, 61, 5))
ax1.set_yticklabels([f"{i}%" for i in range(40, 61, 5)])
ax1.set_xticks(Assist.index[::2])
ax1.fill_between(Assist.index, 36, isoPct, color="green", alpha=0.3, label="ISO baskets")
ax1.plot(Assist.index, assistPct, marker="o", color="red", label="Assist Percentage")

plt.xlabel("Seasons")
plt.ylabel("Percentage")
plt.title("Assisted vs Isolation Baskets")
plt.legend()
plt.show()


# ---------------------------------
# 3-POINT EFFICIENCY ANALYSIS
# ---------------------------------
fig, ax1 = plt.subplots(figsize=(12,6))

ax2 = ax1.twinx()

EFG = final_df.groupby("SEASON")[["EFG_PCT"]].mean() * 100
ax1.plot(EFG.index, EFG["EFG_PCT"], color="green", marker="o", label="Effective Field Goal %")
ax1.set_yticks(range(47, 55, 1))
ax1.set_yticklabels([f"{i}%" for i in range(47, 55, 1)])
ax1.set_ylabel("Effective Field Goal %", color="green")

threePt = final_df.groupby("SEASON")[["FG3A", "FG3M"]].mean()
ax2.plot(threePt.index, threePt["FG3A"], color="red", marker="o", label="3-Points Attempted")
ax2.set_xticks(threePt.index[::2])
ax2.set_ylabel("3-Points Attempted", color="red")

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc="upper left")
plt.title("3-Point Efficiency Overtime")
plt.show()
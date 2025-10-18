# Data Dictionary
| **Column Name** | **Description**                                                      | **Type** | **Category**    |
| --------------- | -------------------------------------------------------------------- | -------- | --------------- |
| **TEAM_NAME**   | Name of the NBA team.                                                | String   | Identifier      |
| **GP**          | Games played in the season.                                          | Integer  | Counting Stat   |
| **W**           | Number of wins.                                                      | Integer  | Counting Stat   |
| **L**           | Number of losses.                                                    | Integer  | Counting Stat   |
| **W_PCT**       | Win percentage (W ÷ GP).                                             | Float    | Derived Metric  |
| **FGM**         | Field goals made.                                                    | Integer  | Counting Stat   |
| **FGA**         | Field goals attempted.                                               | Integer  | Counting Stat   |
| **FG_PCT**      | Field goal percentage (FGM ÷ FGA).                                   | Float    | Efficiency      |
| **FG3M**        | Three-point field goals made.                                        | Integer  | Counting Stat   |
| **FG3A**        | Three-point field goals attempted.                                   | Integer  | Counting Stat   |
| **FG3_PCT**     | Three-point percentage (FG3M ÷ FG3A).                                | Float    | Efficiency      |
| **FTM**         | Free throws made.                                                    | Integer  | Counting Stat   |
| **FTA**         | Free throws attempted.                                               | Integer  | Counting Stat   |
| **FT_PCT**      | Free throw percentage (FTM ÷ FTA).                                   | Float    | Efficiency      |
| **OREB**        | Offensive rebounds.                                                  | Integer  | Counting Stat   |
| **DREB**        | Defensive rebounds.                                                  | Integer  | Counting Stat   |
| **REB**         | Total rebounds (OREB + DREB).                                        | Integer  | Counting Stat   |
| **AST**         | Assists.                                                             | Integer  | Counting Stat   |
| **TOV**         | Turnovers.                                                           | Integer  | Counting Stat   |
| **STL**         | Steals.                                                              | Integer  | Counting Stat   |
| **BLK**         | Blocks made.                                                         | Integer  | Counting Stat   |
| **BLKA**        | Shots blocked against (times a team’s shot was blocked).             | Integer  | Counting Stat   |
| **PF**          | Personal fouls committed.                                            | Integer  | Counting Stat   |
| **PFD**         | Personal fouls drawn.                                                | Integer  | Counting Stat   |
| **PTS**         | Total points scored (2×FGM + 3×FG3M + FTM).                          | Integer  | Counting Stat   |
| **PLUS_MINUS**  | Net point differential when team is on the floor.                    | Float    | Derived Metric  |
| **SEASON**      | NBA season (e.g., 2020–21).                                          | String   | Identifier      |
| **OFF_RATING**  | Points scored per 100 possessions.                                   | Float    | Advanced Metric |
| **DEF_RATING**  | Points allowed per 100 possessions.                                  | Float    | Advanced Metric |
| **NET_RATING**  | OFF_RATING − DEF_RATING (overall team efficiency).                   | Float    | Advanced Metric |
| **AST_PCT**     | Percentage of team field goals assisted.                             | Float    | Advanced Metric |
| **AST_TO**      | Assist-to-turnover ratio.                                            | Float    | Advanced Metric |
| **AST_RATIO**   | Assists per 100 possessions.                                         | Float    | Advanced Metric |
| **OREB_PCT**    | Offensive rebound percentage (team OREB ÷ available OREB).           | Float    | Advanced Metric |
| **DREB_PCT**    | Defensive rebound percentage.                                        | Float    | Advanced Metric |
| **REB_PCT**     | Total rebound percentage.                                            | Float    | Advanced Metric |
| **TM_TOV_PCT**  | Turnover percentage (turnovers per 100 possessions).                 | Float    | Advanced Metric |
| **EFG_PCT**     | Effective field goal percentage = (FGM + 0.5×FG3M) ÷ FGA.            | Float    | Efficiency      |
| **TS_PCT**      | True shooting percentage = PTS ÷ (2×(FGA + 0.44×FTA)).               | Float    | Efficiency      |
| **PACE**        | Estimated possessions per 48 minutes.                                | Float    | Tempo Metric    |
| **POSS**        | Estimated total team possessions.                                    | Float    | Tempo Metric    |
| **PIE**         | Player Impact Estimate (team’s contribution to overall game events). | Float    | Advanced Metric |

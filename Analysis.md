# Analysis 🗣️

Avid basketball fans watch today’s NBA games and relish the claim that, “The game isn’t as good as it used to be,” or that, “Teams then were better than teams now.” For this project, I examined how teams’ statistical profiles have evolved since 2000, highlighting trends in scoring, pace, and shot selection, and exploring what teams have chosen to prioritize as the years have gone on.

The objective of this analysis is to explore how team strategies have changed over time using both basic statistics and advanced metrics. As a basketball fan myself, I’ve included context within each analysis to explain any irregularities, inconsistencies, or anomalies. The goal is to identify trends in shooting behavior, game pace, defensive performance, and overall team efficiency.

Data was collected from official NBA box scores and advanced statistics spanning the 2000 to 2025 seasons. The dataset includes both basic counting stats (e.g., field goals, assists, rebounds) and advanced metrics (e.g., pace, offensive/defensive ratings, plus-minus). Missing values for counting stats were filled with zeros, while percentages and advanced metrics were left as NaN to preserve historical accuracy.

**Note:** During the 2011-12 season, there was a lockout due to a labor dispute and that year's regular season have been reduced to only 66 games rather than the normal 82 games. Plus a noticeable dip appears around 2020-21 season likely due to pandemic-related disruptions.

---

## Pace vs Possessions
<img width="1070" height="547" alt="Pace vs Possessions" src="https://github.com/user-attachments/assets/2070f74b-d2fd-4816-a194-5fad292c92b1" />
This chart compares how Pace (possessions per 48 minutes) and total Possessions changed from 2000–01 to 2024–25. The data shows that the tempo of NBA games has steadily gone up, especially after 2013 — reflecting how teams started playing faster and emphasizing offense more.

After being fairly stable in the early 2000s, both pace and possessions began climbing in the mid-2010s. That shift lines up with the rise of small-ball lineups, transition-heavy play, and the growing importance of 3-point shooting.
The 2014–19 Golden State Warriors were the best example of this change — their fast-paced, motion-based offense pushed spacing and tempo to new levels, influencing the entire league. Similarly, Mike D’Antoni’s “Seven Seconds or Less” Phoenix Suns (2004–08) helped start this trend years earlier, setting the stage for the pace revolution that came later.

Overall, the steady increase in pace and possessions over the past decade demonstrates the league’s prioritization of speed, spacing, and offensive efficiency — core components of modern basketball strategy.


## Defensive Strategy
<img width="1189" height="790" alt="Defense" src="https://github.com/user-attachments/assets/1fef9ac0-9cdb-4d9c-b39c-f6df179387d1" />
This graph compares Defensive Rating with total steals and blocks per season to show how team defense has evolved. This data highlights the league's overall defense and what teams prioritized, adapting to offense-oriented strategies.

Over time, Defensive Ratings have gone up — meaning defenses have found it harder to keep up with today’s faster, more spaced-out offenses. As three-point volume increased, defenses had to cover more ground, rotate faster, and defend more in transition.
Back in the 2000s, teams like the 2004 Detroit Pistons and 2008–2014 Boston Celtics were built on physical, half-court defense. These teams slowed the game down and forced opponents into tough midrange shots. Modern defensive powerhouses like the 2019 Raptors or 2022–23 Celtics, however, rely more on switchability and versatility — using athletic wings and mobile bigs to guard multiple positions.

Overall, the data shows that while individual statistics like blocks and steals have not changed too much throughout the years, the league's overall defense is struggling to keep up with the growing dominance in offensive game.


## Rebounding Strategy
<img width="1010" height="584" alt="Rebounding Strategy (Every 5 Seasons)" src="https://github.com/user-attachments/assets/e4a5ad3b-f580-4c3c-a326-6be95b494c8b" />
This graph shows a box chart comparison of the league's offensive and defensive rebounding percentage for every 5 seasons. This data highlights teams priority in defensive bigs to grab defensive boards in order to gain more offensive opportunities.

Since the 2012-13 season, Defensive Rebounding percentage shows an increase while Offensive rebounding has been decreasing. This reflects how the league shifts away from getting offensive boards to getting back on transition defense so as to prevent fast breaks rather than fighting for offensive boards for a second field goal attempt.
For example, during the 2010s San Antonio Spurs and Golden State Warriors’ dynasties, both teams emphasized quickly retreating on defense after missed shots rather than contesting offensive boards. Conversely, early 2000s teams such as the Detroit Pistons or San Antonio Spurs (2003–07) often relied heavily on offensive rebounds to generate extra possessions through dominant bigs like Ben Wallace and Tim Duncan.

Overall, this represents how teams are prioritizing more on pace control and quickly going back on defense as it is more risky to grab offensive rebounds due to current offense being so spread out.


## Overall Scoring Efficiency
<img width="1074" height="547" alt="Scoring Efficiency" src="https://github.com/user-attachments/assets/d27ffc75-30a5-41a5-8151-89560e833c94" />
<img width="1074" height="528" alt="3-Point Efficiency" src="https://github.com/user-attachments/assets/7e6485db-dfe9-4746-b4a0-d2fc39f883a2" />
These graphs represent the league's scoring efficiency. This data highlights the sharp increase in the league's overall offensive output and scoring efficiency, especially utilizing the 3-pointers. From the early 2000s to the mid-2010s, league-wide True Shooting(TS%) and Effective Field Goal(EFG%) percentages showed slow growth. However, starting around 2015–16, both metrics began a sharp upward trend, marking the start of a new offensive era in the NBA.

When viewed alongside the second chart, this point aligns almost perfectly with a surge in 3-point attempts. Between 2015 and 2025, teams have increased their 3-point volume by more than double, while maintaining or even improving 3-point Effective Field Goal percentage, which rose from around 49–50% to over 54%. This indicates that teams didn’t just shoot more threes, they became significantly better at making them. The rise of 3-point efficiency and overall scoring metrics(TS% and EFG%) suggests that the three-point shot has become the single greatest contributor to modern offensive efficiency.
The Golden State Warriors(2014–19) redefined offensive efficiency by leveraging spacing, off-ball motion, and high-volume three-point shooting. Their success encouraged other franchises — notably the Houston Rockets(2017–20) under Daryl Morey — to push shot selection to the analytical extreme, eliminating midrange shots almost entirely in favor of threes and layups.

Meanwhile, total field goal attempts also trended upward, but not as sharply, implying that teams achieved higher scoring outputs without drastically increasing shot volume, but rather by optimizing shot their selection(fewer midrange, more 3s and shots near the rim).


## Assists vs Isolation Baskets
<img width="1010" height="547" alt="Assists vs Iso" src="https://github.com/user-attachments/assets/2a4aa397-0b36-430e-b5bf-fcae26105238" />
This graph represents the league's percentage in isolation baskets and assists baskets. This data highlights how the league's offensive game has shifted away from isolation offense to distributing the ball amongst teammates in order to get wide-open easy baskets.

From 2000–2009, isolation-heavy playstyles — influenced by streetball culture — dominated offenses before analytics-driven motion systems took over. Stars like Allen Iverson, Kobe Bryant, and Tracy McGrady built their games on one-on-one scoring. In contrast, the 2014–15 San Antonio Spurs showcased the pinnacle of team-oriented, ball-movement offense, often recording some of the league’s highest assist percentages while maintaining elite scoring efficiency.

Overall, this represents the shift in style from an individual playstyle to a more team-oriented playstyle.

---

## Dashboard Analysis
**Pace Overtime:** The league pace has steadily increased since 2013, indicating a shift toward a faster, more transition-focused game. This trend aligns with the rise of small-ball (smaller & faster players) lineups and a higher volume of possessions per game, contributing to increased scoring and more dynamic playstyles.</br>

**Assists to Effective Field-Goal Percentage:** Teams with higher assist numbers tend to have better effective field-goal percentages, suggesting that ball movement and unselfish play are key drivers of offensive efficiency. This is shown by the San Antonio Spurs, whose offense has historically emphasized passing and team-oriented play, resulting in consistently high effective field-goal percentages.</br>

**League Shot Selection:** Over time, 3-point attempts have increased significantly, while mid-range shots have declined. This reflects a league-wide shift toward analytics-based shot selection, prioritizing efficiency, either shooting from beyond the arc or close to the basket. Free throw rates have remained relatively stable, indicating that while shot locations are changing, physicality and fouls drawn have not changed as dramatically.</br>

****Eras dropdown** to compare 2000s, 2010s, and 2020s era.
****Seasons dropdown** to look at league performance per season.
****Top teams table** to show the top 10 teams during the selected era or year.

---

Over the past 25 years, the NBA has evolved from a midrange and isolation-heavy league into a data-driven style centered around pace, spacing, and efficiency. The modern game reflects the direct influence of analytics on coaching philosophy, prioritizing shot quality over volume, versatility over size, and transition opportunities over offensive rebounding. This transformation underscores how deeply statistical insights now shape strategic decisions at every level of basketball.

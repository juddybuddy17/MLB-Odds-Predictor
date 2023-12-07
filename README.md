# DSI-Capstone - MLB Odds Predictor

### Problem Statement
MLB Outcomes App
I want to build a baseball betting consulting app that can guide sports bettors to smarter betting decisions. I have been given game data from Retrosheet that has the stats for each game with the respective home and visiting teams game statistics.   

### Data Collection and Cleaning
I sought guidance from my friend Adam when struggling to find usable data, and he directed me to Retrosheet game data. I gathered game records spanning the last 33 years, commencing from the seismic 1989 World Series. To align with Retrosheet's data dictionary, I meticulously relabeled column names. For my target variables, I introduced columns for run differentials, total runs, home team win/loss, and visitor team win/loss. To enhance data quality, I addressed missing values, removed redundant columns, and binarized boolean features. Leveraging the pandas rolling sum function, I transformed certain features to capture historical trends over the standard 162-game season. Additionally, I engineered new features by calculating ratios between existing ones to derive averages. Finally, I split the data frame at the year 2020 to create a testing dataset for model evaluation.

## Data Dictionary
Field(s)  Meaning
    1     Date in the form "yyyymmdd"
    2     Number of game:
             "0" -- a single game
             "1" -- the first game of a double (or triple) header
                    including seperate admission doubleheaders
             "2" -- the second game of a double (or triple) header
                    including seperate admission doubleheaders
             "3" -- the third game of a triple-header
             "A" -- the first game of a double-header involving 3 teams
             "B" -- the second game of a double-header involving 3 teams
    3     Day of week  ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
  4-5     Visiting team and league
    6     Visiting team game number
          For this and the home team game number, ties are counted as
          games and suspended games are counted from the starting
          rather than the ending date.
  7-8     Home team and league
    9     Home team game number
10-11     Visiting and home team score (unquoted)
   12     Length of game in outs (unquoted).  A full 9-inning game would
          have a 54 in this field.  If the home team won without batting
          in the bottom of the ninth, this field would contain a 51.
   13     Day/night indicator ("D" or "N")
   14     Completion information.  If the game was completed at a
          later date (either due to a suspension or an upheld protest)
          this field will include:
             "yyyymmdd,park,vs,hs,len" Where
          yyyymmdd -- the date the game was completed
          park -- the park ID where the game was completed
          vs -- the visitor score at the time of interruption
          hs -- the home score at the time of interruption
          len -- the length of the game in outs at time of interruption
          All the rest of the information in the record refers to the
          entire game.
   15     Forfeit information:
             "V" -- the game was forfeited to the visiting team
             "H" -- the game was forfeited to the home team
             "T" -- the game was ruled a no-decision
   16     Protest information:
             "P" -- the game was protested by an unidentified team
             "V" -- a disallowed protest was made by the visiting team
             "H" -- a disallowed protest was made by the home team
             "X" -- an upheld protest was made by the visiting team
             "Y" -- an upheld protest was made by the home team
          Note: two of these last four codes can appear in the field
          (if both teams protested the game).
   17     Park ID
   18     Attendance (unquoted)
   19     Time of game in minutes (unquoted)
20-21     Visiting and home line scores.  For example:
             "010000(10)0x"
          Would indicate a game where the home team scored a run in
          the second inning, ten in the seventh and didn't bat in the
          bottom of the ninth.
22-38     Visiting team offensive statistics (unquoted) (in order):
             at-bats
             hits
             doubles
             triples
             homeruns
             RBI
             sacrifice hits.  This may include sacrifice flies for years
                prior to 1954 when sacrifice flies were allowed.
             sacrifice flies (since 1954)
             hit-by-pitch
             walks
             intentional walks
             strikeouts
             stolen bases
             caught stealing
             grounded into double plays
             awarded first on catcher's interference
             left on base
39-43     Visiting team pitching statistics (unquoted)(in order):
             pitchers used ( 1 means it was a complete game )
             individual earned runs
             team earned runs
             wild pitches
             balks
44-49     Visiting team defensive statistics (unquoted) (in order):
             putouts.  Note: prior to 1931, this may not equal 3 times
                the number of innings pitched.  Prior to that, no
                putout was awarded when a runner was declared out for
                being hit by a batted ball.
             assists
             errors
             passed balls
             double plays
             triple plays
50-66     Home team offensive statistics
67-71     Home team pitching statistics
72-77     Home team defensive statistics
78-79     Home plate umpire ID and name
80-81     1B umpire ID and name
82-83     2B umpire ID and name
84-85     3B umpire ID and name
86-87     LF umpire ID and name
88-89     RF umpire ID and name
          If any umpire positions were not filled for a particular game
          the fields will be "","(none)".
90-91     Visiting team manager ID and name
92-93     Home team manager ID and name
94-95     Winning pitcher ID and name
96-97     Losing pitcher ID and name
98-99     Saving pitcher ID and name--"","(none)" if none awarded
100-101   Game Winning RBI batter ID and name--"","(none)" if none
          awarded
102-103   Visiting starting pitcher ID and name
104-105   Home starting pitcher ID and name
106-132   Visiting starting players ID, name and defensive position,
          listed in the order (1-9) they appeared in the batting order.
133-159   Home starting players ID, name and defensive position
          listed in the order (1-9) they appeared in the batting order.
  160     Additional information.  This is a grab-bag of informational
          items that might not warrant a field on their own.  The field 
          is alpha-numeric. Some items are represented by tokens such as:
             "HTBF" -- home team batted first.
             Note: if "HTBF" is specified it would be possible to see
             something like "01002000x" in the visitor's line score.
          Changes in umpire positions during a game will also appear in 
          this field.  These will be in the form:
             umpchange,inning,umpPosition,umpid with the latter three
             repeated for each umpire.
          These changes occur with umpire injuries, late arrival of 
          umpires or changes from completion of suspended games. Details
          of suspended games are in field 14.
  161     Acquisition information:
             "Y" -- we have the complete game
             "N" -- we don't have any portion of the game
             "D" -- the game was derived from box score and game story
             "P" -- we have some portion of the game.  We may be missing
                    innings at the beginning, middle and end of the game.
 
Missing fields will be NULL.

### EDA
I explored certain features by comparing them to y-variables and other features that make up the y-variable. I did not realize there were ties in baseball and it turns out I found a crazy game on 9/30/2001 where a day game between the Orioles and the Yankees went 15 innings, over 5 hours, and the game ended in a tie at 1-1. I created a correlation heat map to show how well certain features relate to each other and there are bar graphs to show the overall run differential and wins-loss for each team over the last 33 years.

### Preprocessing and Modeling

Incorporating additional features such as RBIs, stolen base success rates, runners left on base, strikeout ratios, and walk ratios. I wanted to frame the models mostly on offense and hitting statistics, but there some features I could not avoid like earned runs, errors, and double plays. Even the the defensive and pitching data is a bit dull I still wanted to include it to get the best model possible. My training data spanned the years 1989 to 2000, while the testing data covered games from 2001 to 2002. Utilizing One Hot Encoder for categorical columns like ballpark and manager, I observed that these factors didn't significantly impact the model, prompting me to focus predominantly on numerical data. To streamline the classification task, I excluded games resulting in ties, concentrating solely on outcomes categorized as wins or losses.

My best models results are as follows:
Run Differential - Random Forest Regressor  - 86.3% R2 score
Total Runs - Linear Regression - 86.4% R2 score
winner - Random Forest Classifier - 91.8% Accuracy

### Conclusion and Recommendations
In conclusion, the developed models exhibit a certain level of confidence, however, there remains room for further refinement through additional feature engineering to gauge their impact on predictive accuracy. Future iterations could consider incorporating more comprehensive pitching statistics such as WHIP, ERA, K/9, and HR/9 to enhance the models' predictive capabilities. Exploring individual player strengths and assessing how they influence overall game outcomes could offer valuable insights for more nuanced predictions. Additionally, a commitment to regularly updating the game data will ensure the incorporation of the most up-to-date statistics, maintaining the models' relevance and accuracy over time. This iterative approach to feature enhancement and continuous data updating will contribute to the models' ongoing effectiveness and adaptability.

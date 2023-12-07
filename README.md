# DSI-Capstone - MLB Odds Predictor

### Problem Statement
I want to build a baseball betting consulting app that can guide sports bettors on educated betting decisions. I downloaded data from retrosheet.org that has the stats for each game with the respective home and visiting teams game statistics.      

### Data Collection and Cleaning
I sought guidance from my friend Adam when struggling to find usable data, and he directed me to Retrosheet game data. I gathered game records spanning the last 33 years, commencing from the seismic 1989 World Series. To align with Retrosheet's data dictionary, I meticulously relabeled column names. For my target variables, I introduced columns for run differentials, total runs, home team win/loss, and visitor team win/loss. To enhance data quality, I addressed missing values, removed redundant columns, and binarized boolean features. Leveraging the pandas rolling sum function, I transformed certain features to capture historical trends over the standard 162-game season. Additionally, I engineered new features by calculating ratios between existing ones to derive averages. Finally, I split the data frame at the year 2020 to create a testing dataset for model evaluation.

## Data Dictionary
"Guide to Retrosheet Game Logs" at https://www.retrosheet.org/gamelogs/index.html

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

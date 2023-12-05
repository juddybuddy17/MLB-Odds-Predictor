import pickle
import streamlit as st
import pandas as pd

with open('../Models/WinsLosses.pkl', 'rb') as file:
    pipe_log = pickle.load(file)
with open('../Models/TotalRuns.pkl', 'rb') as file:
    pipe_tot = pickle.load(file)
with open('../Models/RunDiff.pkl', 'rb') as file:
    pipe_lr = pickle.load(file)

st.title('MLB Outcomes')

games = pd.read_csv('../Data/Created/MLBgames.csv')
seasons = pd.read_csv('../Data/Created/seasons.csv')
teams = pd.read_csv('../Data/Created/streamlitTEAMS.csv')

feature1 = st.selectbox("Home Team", teams['team'])
feature2 = st.selectbox("Home Year", seasons['0'])
feature3 = st.selectbox("Away Team", teams['team'])
feature4 = st.selectbox("Away Year", seasons['0'])

row = games[
    (games['home_team'] == feature1) & (games['season'] == int(feature2)) &
    (games['visitor_team'] == feature3) & (games['season'] == int(feature4))
]

print("Selected Row:",row)

if row.empty:
    st.write("No game found. Try another input")
else:
# Win Team
    features_for_prediction = row[['v_ba', 'h_ba', 'v_obp', 'h_obp', 'v_slg', 'h_slg', 'v_ops', 'h_ops', 'v_runs', 'home_team', 'visitor_team']]

    prediction = pipe_log.predict(features_for_prediction)

    prediction_label = 'Home Team Win' if prediction == 1 else 'Away Team Win'
    st.write('Prediction:', prediction_label)
# Run Differential
    features_for_prediction = row[['v_ba', 'h_ba', 'v_obp', 'h_obp', 'v_slg', 'h_slg', 'v_ops', 'h_ops', 'v_runs', 'home_team', 'visitor_team']]

    prediction = pipe_lr.predict(features_for_prediction)
    
    st.write('Run Differential:', prediction)

# Total Runs
    features_for_prediction = row[['v_ba', 'h_ba', 'v_obp', 'h_obp', 'v_slg', 'h_slg', 'v_ops', 'h_ops', 'v_runs', 'home_team', 'visitor_team']]

    prediction = pipe_tot.predict(features_for_prediction)
    
    st.write('Total Runs:', prediction)
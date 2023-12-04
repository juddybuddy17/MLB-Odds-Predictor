import pickle
import streamlit as st
import pandas as pd

with open('../Models/TotalRuns.pkl', 'rb') as file:
    pipe = pickle.load(file)

st.title('MLB Outcomes')

games = pd.read_csv('../Data/Created/MLBgames.csv')
seasons = pd.read_csv('../Data/Created/seasons.csv')
teams  = pd.read_csv('../Data/Created/streamlitTEAMS.csv')

feature1 = st.selectbox("Home Team", teams['team'])
feature2 = st.selectbox("Home Year", seasons['0'])
feature3 = st.selectbox("Away Team", teams['team'])
feature4 = st.selectbox("Away Year", seasons['0'])

selected_row = games[
    (games['home_team'] == feature1) & (games['season'] == int(feature2)) & 
    (games['visitor_team'] == feature3) & (games['season'] == int(feature4))
]

print("Selected Row:", selected_row)

if selected_row.empty:
    st.write("No game found. Try another input")
else:
    features_for_prediction = selected_row['v_ba','h_ba','v_obp','h_obp','v_slg','h_slg','v_ops','h_ops','v_roll_rbis','v_roll_tbs','v_bb_rat','v_sb_rat','h_bb_rat','h_sb_rat','v_k_rat','h_k_rat','home_team','visitor_team','park_id']

    prediction = pipe.predict(features_for_prediction)
    
    prediction_label = 'Home Team Win' if prediction == 1 else 'Away Team Win'
    st.write('Prediction:', prediction_label)
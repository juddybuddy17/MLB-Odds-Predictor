import pickle
import streamlit as st
import pandas as pd

with open('../Models/WinsLosses.pkl', 'rb') as file:
    ct_wins_losses = pickle.load(file)
with open('../Models/TotalRuns.pkl', 'rb') as file:
    ct_total_runs = pickle.load(file)
with open('../Models/RunDiff.pkl', 'rb') as file:
    ct_run_diff = pickle.load(file)

st.title('MLB Outcomes')

games = pd.read_csv('../Data/Created/MLBgames.csv')

h_unique_teams = games['h_nick_name'].unique()
v_unique_teams = games['v_nick_name'].unique()

feature1 = st.selectbox("Home Team", h_unique_teams)
feature2 = st.selectbox("Away Team", v_unique_teams)

# Button to trigger predictions
if st.button('Batter Up'):
    row = games.loc[(games['h_nick_name'] == feature1) & (games['v_nick_name'] == feature2)]

    features_for_prediction = row[['v_ba', 'h_ba', 'v_obp', 'h_obp', 'v_slg', 'h_slg', 'v_ops', 'h_ops', 'v_roll_rbis',
                                   'v_roll_tbs', 'v_bb_rat', 'v_sb_rat', 'h_bb_rat', 'h_sb_rat', 'v_k_rat', 'h_k_rat',
                                   'v_runs', 'home_team', 'visitor_team', 'park_id']]

    all_columns = ['v_ba', 'h_ba', 'v_obp', 'h_obp', 'v_slg', 'h_slg', 'v_ops', 'h_ops', 'v_roll_rbis', 'v_roll_tbs',
                   'v_bb_rat', 'v_sb_rat', 'h_bb_rat', 'h_sb_rat', 'v_k_rat', 'h_k_rat', 'v_runs', 'home_team',
                   'visitor_team', 'park_id']

    subset_for_prediction_df = pd.DataFrame(columns=all_columns)

    subset_for_prediction_df[features_for_prediction.columns] = features_for_prediction

    missing_columns = set(all_columns) - set(features_for_prediction.columns)
    for col in missing_columns:
        subset_for_prediction_df[col] = 0

    # Run Differential
    prediction_run_diff = ct_run_diff.predict(subset_for_prediction_df)
    rounded_run_diff = round(prediction_run_diff[-1] * 2) / 2
    st.write('Run Differential: {:.1f}'.format(rounded_run_diff))

    # Total Runs
    prediction_total_runs = ct_total_runs.predict(subset_for_prediction_df)
    rounded_total_runs = round(prediction_total_runs[-1] * 2) / 2
    st.write('Total Runs: {:.1f}'.format(rounded_total_runs))

    # Wins Loss
    winning_team = feature1 if rounded_run_diff > 0 else feature2
    st.write('Favorited: {}'.format(winning_team))
    st.write('$Show$ $Me$ $The$ $Money!!$')
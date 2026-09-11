import streamlit as st 
import pandas as pd
import datetime
from database import insert_round, insert_range_session, get_club_average

def streamlit_input():
    tab1, tab2 = st.tabs(["Round Score Input", "Range Session Input"])
    with tab1:
        st.title("Golf Tracker App")
        st.header("Track your golf scores and performance over time")
        score = st.number_input("Enter round score:", min_value=0)
        date = st.date_input("Date:")
        if st.button("Submit"):
            insert_round(score, date)
            st.success("Round score submitted successfully!")
    with tab2:
        st.title("Range Session Input")
        st.header("Track your average driving distances")
        option = st.selectbox(
            "Golf Club",
        [
                "Driver",
                "3 Wood",
                "5 Wood",
                "7 Wood",
                "3 Hybrid",
                "3 Iron",
                "4 Iron",
                "5 Iron", 
                "6 Iron", 
                "7 Iron",
                "8 Iron",
                "9 Iron",
                "52 Degree Wedge",
                "54 Degree Wedge",
                "56 Degree Wedge",
                "58 Degree Wedge",
                "60 Degree Wedge",
                "Pitching Wedge",
            "Sand Wedge",
        ],
        index=None,
        placeholder=" Select a club or add a new one",
        accept_new_options=True,
        )
        distance = st.number_input("Enter distance (in yards):", min_value=0)
        if st.button("Submit Range distance"):
            insert_range_session(option, distance)
            st.success("Range session submitted successfully!")


def display_data():
    st.title("Distance Averages by Club")
    averages = get_club_average()
    df = pd.DataFrame(averages, columns=["Club", "Average Distance (yards)"])
    st.dataframe(df)

streamlit_input()
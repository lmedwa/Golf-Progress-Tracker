import streamlit as st 
import pandas as pd
import datetime
from database import insert_round, insert_range_session, get_club_average

def streamlit_input():
    tab1, tab2 = st.tabs(["Round Score Input", "Range Session Input"])
    with tab1:
        st.title("Golf Tracker App")
        st.header("Track your golf scores and performance over time")
        course_rating = st.number_input("Enter course rating:", min_value=0)
        slope_rating = st.number_input("Enter slope rating:", min_value=0)
        date = st.date_input("Date:")
        nine_or_eighteen = st.selectbox(
            " Are you playing 9 or eighteen holes",
            ("9", "18")
        )
        scores = []
        if nine_or_eighteen == "9":
            cols = st.columns(9)
            for i, col in enumerate(cols):
                with col:
                    hole = st.number_input(f"Hole {i+1}:", min_value=0)
                    scores.append(hole)

        elif nine_or_eighteen == "18":
            cols = st.columns(18)
            for i, col in enumerate(cols):
                with col:
                    hole = st.number_input(f"Hole {i+1}:", min_value=0)
                    scores.append(hole)

        total_score = sum(scores)
        st.write(f"Total Score: {total_score}")

        if st.button("Submit"):
            insert_round(total_score, date, course_rating, slope_rating)
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
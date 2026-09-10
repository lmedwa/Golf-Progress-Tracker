import streamlit as st 
import datetime
from database import insert_round

def streamlit_input():
    st.title("Golf Tracker App")
    st.header("Track your golf scores and performance over time")
    score = st.number_input("Enter round score:", min_value=0)
    date = st.date_input("Date:")
    if st.button("Submit"):
        insert_round(score, date)




def main():
    streamlit_input()
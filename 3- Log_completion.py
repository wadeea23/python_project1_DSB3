import pandas as pd 
import time 
import datetime
import streamlit as st
import utils
import requests

st.subheader("Log Habit")
df = utils.load_data()
active_habits = df[df["Status"] == "Active"]
habit_complete = st.selectbox("Which habit was completed?",active_habits["Habit"])
if st.button("Log_completion"):
    completion_time = datetime.datetime.now()
    st.write("Habit:", habit_complete)
    st.write("Completed at:", completion_time)
    quote, author = utils.daily_quote()
    st.success("Habit completed!")
    st.info(f" {quote}")
    st.write(f" {author}")    



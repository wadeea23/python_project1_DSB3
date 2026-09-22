import pandas as pd 
import time 
import datetime
import streamlit as st
import utils
import requests
df = utils.load_data()
st.subheader("Add New Habit")
habit = st.text_input("Habit name")
frequency = st.selectbox( "Frequency",("Daily", "Weekly", "Monthly"))
target = st.text_input("Target goal")
category = st.selectbox("Category",("Health", "Productivity", "Learning", "Other"))
start_date = st.date_input("Start date",datetime.date.today())
if st.button("Add Habit"): 
    new_habit = {
        "Habit": habit,
        "Frequency": frequency,
        "Target": target,
        "Category": category,
        "Start Date": start_date,
        "Status": "Active" }

    df = df._append(new_habit, ignore_index=True)
    utils.save_data(df)
    st.success("Habit added successfully!")

    

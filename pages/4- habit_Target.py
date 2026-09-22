import pandas as pd 
import time 
import datetime
import streamlit as st
import utils
import requests

st.subheader("Habit Target")
df = utils.load_data()
target_df = utils.show_target(df)
st.dataframe(target_df)
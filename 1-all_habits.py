import pandas as pd 
import time 
import datetime
import streamlit as st
import utils
import requests

st.subheader("ALL Habit")
log_com =utils.load_data()
st.write(log_com)

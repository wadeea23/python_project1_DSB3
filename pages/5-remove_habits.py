import pandas as pd 
import time 
import datetime
import streamlit as st
import utils
import requests
st.subheader("Remove/Edit Habit")
log_com =utils.load_data()
st.write(log_com)
st.button("Update", type="primary")
edited_df = st.data_editor(log_com, num_rows="dynamic")
utils.update_data(edited_df)



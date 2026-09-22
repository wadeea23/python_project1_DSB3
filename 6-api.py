import streamlit as st
import utils

quote, author = utils.daily_quote()

st.write("Motivational Quote")
st.write(quote)
st.write("--" + author)
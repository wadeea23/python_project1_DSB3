import pandas as pd 
import datetime
import streamlit as st
#import utils
import requests
#from openai import OpenAI

st.title("Habit_Tracker")

video_file = open("Habit_Tracker.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)

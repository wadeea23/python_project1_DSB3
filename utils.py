import pandas as pd
import streamlit as st
import time 
import datetime
import requests
from openai import OpenAI

def load_data():
    data = pd.read_csv("Habits.csv")
    return data
def update_data(df):
    df.to_csv('Habits.csv',index = False)

def save_data(df):
    df.to_csv('Habits.csv',index = False)

def show_target(df):
    return df[["Habit", "Target"]]

def log_habit(df, habit):
    timestamp = datetime.datetime.now()
    df.loc[df["Habit"] == habit, "Last Completed"] = timestamp
    update_data(df)
    return df  


#def daily_quote():
    #response = requests.get("https://zenquotes.io/api/quotes")
    #data = response.json()
    #quote = data[0]["q"]
    #author = data[0]["a"]
    #return quote, author 


    
def daily_quote():
    response = requests.get("https://dummyjson.com/quotes/random")
    data = response.json()
    quote = data["quote"]
    author = data["author"]
    ### i use this part for translate from chatgpt
    translated = requests.get("https://api.mymemory.translated.net/get",params={"q": quote, "langpair": "en|ar"}).json()
    arabic_quote = translated["responseData"]["translatedText"]
    return arabic_quote, author
print(daily_quote())








openai_api_key = st.secrets["OPENAI_API_KEY"]
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY")
client = OpenAI( base_url="https://openrouter.ai/api/v1",api_key=openai_api_key)
def get_llm_response(prompt):
    completion = client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        messages=[
            {
                "role": "system",
                "content": "you are a personal habit coach, Give simple advice in Arabic",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )

    response = completion.choices[0].message.content
    return response












    

    

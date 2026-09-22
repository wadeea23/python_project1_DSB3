import streamlit as st
import utils


st.title("personal Habit")
habit = st.text_input("Enter your habit")
streak = st.text_input("Current streak")
completion_rate = st.text_input("Completion rate")

if st.button("Get Advice"):

    prompt = f"""
    My habit is {habit}.
    My current streak is {streak} days.
    My completion rate is {completion_rate}.

    Give me one short advice and one habit stacking idea.
    """
    advice = utils.get_llm_response(prompt)
    st.write(advice)
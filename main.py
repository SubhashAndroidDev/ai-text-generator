import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Text Generator")

prompt = st.text_area("Enter your prompt")

if st.button("Generate"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt")
    else:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        st.write(response.choices[0].message.content)
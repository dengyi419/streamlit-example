import streamlit as st
import openai

openai.api_key = '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'

st.title('Chat with GPT-3')

user_input = st.text_input("You: ")

if user_input:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=60
    )

    st.text("GPT-3: " + response.choices[0].text.strip())

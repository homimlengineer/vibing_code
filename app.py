import streamlit as st
import openai
import os

client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

st.title("🎧 Vibe Coder — Prompt Your Feeling Into Code")

vibe = st.text_area("Describe the vibe or feeling (e.g. 'like a jazz club at midnight')")

if st.button("Generate Code"):
    with st.spinner("Vibing..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You're a creative assistant that turns vibes and feelings into functional code or UI ideas."},
                {"role": "user", "content": f"Create a webpage based on this vibe: {vibe}"}
            ]
        )
        st.code(response.choices[0].message.content, language="html")

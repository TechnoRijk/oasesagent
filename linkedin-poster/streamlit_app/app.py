import streamlit as st
import requests

st.title('LinkedIn Post Generator')

post_content = st.text_area("Post Content")
image_prompt = st.text_input("Image Prompt")
scheduled_time = st.text_input("Scheduled Time (YYYY-MM-DD HH:MM:SS)")

if st.button('Generate and Schedule Post'):
    response = requests.post('http://localhost:5000/api/posts', json={'content': post_content, 'image_prompt': image_prompt, 'scheduled_time': scheduled_time})
    if response.status_code == 200:
        st.success("Post scheduled successfully!")
    else:
        st.error("Error scheduling post.")

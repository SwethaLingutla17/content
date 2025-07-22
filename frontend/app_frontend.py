import os
import requests
import streamlit as st

st.set_page_config(page_title="AI Content Creator", page_icon="🚀", layout="centered")

st.title("🚀 AI Content Creator for Your Business")

backend_url = os.getenv("BACKEND_URL", "http://localhost:8000")

st.write("Fill in the fields below and click **Generate** to create on-brand content.")

content_type = st.selectbox("Content Type", ["Blog Post", "Social Media Caption", "Ad Copy", "Email Promo", "Product Description"])
topic = st.text_input("Topic / Product / Campaign")
tone = st.selectbox("Tone", ["Casual", "Professional", "Witty", "Inspirational", "Bold", "Friendly"])
words = st.number_input("Target Word Count (optional)", min_value=0, value=0, step=50)

if st.button("Generate"):
    if not topic.strip():
        st.error("Please enter a topic first.")
    else:
        payload = {
            "content_type": content_type,
            "topic": topic,
            "tone": tone,
            "words": int(words) if words else None,
        }
        try:
            resp = requests.post(f"{backend_url}/generate", json=payload, timeout=60)
            resp.raise_for_status()
        except Exception as e:
            st.error(f"Request failed: {e}")
        else:
            data = resp.json()
            st.subheader("Generated Content")
            st.write(data.get("content", ""))
            with st.expander("Prompt & Debug Info"):
                st.json(data)

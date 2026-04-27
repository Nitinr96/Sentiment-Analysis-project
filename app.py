import streamlit as st
from textblob import TextBlob

# Page configuration
st.set_page_config(page_title="Sentiment Analyzer", page_icon="📊")

# Header Section
st.title("🧠 Sentiment Analysis Dashboard")
st.markdown("Enter any text below to determine the sentiment.")

# This is how you create a line in Streamlit correctly
st.divider() 

# User Input
user_input = st.text_area("Enter your text here:", placeholder="Type something...")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        blob = TextBlob(user_input)
        score = blob.sentiment.polarity
        
        if score > 0:
            st.success(f"POSITIVE 😄 (Score: {score:.2f})")
        elif score < 0:
            st.error(f"NEGATIVE 😡 (Score: {score:.2f})")
        else:
            st.info(f"NEUTRAL 😐 (Score: {score:.2f})")

st.divider()
st.caption("Powered by Streamlit")

import streamlit as st
from textblob import TextBlob

# Page configuration
st.set_page_config(page_title="Sentiment Analyzer", page_icon="📊")

## Header Section
st.title("🧠 Sentiment Analysis Dashboard")
st.markdown("Enter any text below to determine if the sentiment is **Positive**, **Negative**, or **Neutral**.")

---

## User Input
user_input = st.text_area("Enter your text here:", placeholder="Type something like 'I love this app! It's so helpful.'")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        # Sentiment Logic (Swap this part with your specific model code)
        blob = TextBlob(user_input)
        score = blob.sentiment.polarity
        
        # Determine Sentiment Label and Color
        if score > 0:
            label = "POSITIVE"
            color = "green"
            emoji = "😄"
        elif score < 0:
            label = "NEGATIVE"
            color = "red"
            emoji = "😡"
        else:
            label = "NEUTRAL"
            color = "gray"
            emoji = "😐"

        # Display Results
        st.subheader("Result:")
        st.markdown(f"### The sentiment is :{color}[{label} {emoji}]")
        
        # Optional: Show the raw score
        st.info(f"Confidence Score (Polarity): {score:.2f}")

---
st.caption("Powered by Streamlit and TextBlob")

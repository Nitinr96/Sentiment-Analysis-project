import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analyzer", page_icon="📊")

st.title("🧠 Sentiment Analysis Dashboard")
st.write("Analyze text and see the percentage of sentiment.")

st.divider()

user_input = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter text!")
    else:
        blob = TextBlob(user_input)
        score = blob.sentiment.polarity # This is the -1 to 1 score
        
        # Convert score to percentage
        percentage = abs(score) * 100
        
        if score > 0:
            st.success(f"Positive Sentiment: {percentage:.1f}% 😄")
            st.progress(percentage / 100)
        elif score < 0:
            st.error(f"Negative Sentiment: {percentage:.1f}% 😡")
            st.progress(percentage / 100)
        else:
            st.info("Neutral Sentiment: 100% 😐")
            st.progress(0)

st.divider()

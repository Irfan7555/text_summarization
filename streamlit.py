import streamlit as st
from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

# Streamlit app
st.title("Text Summarization App")

# Input text
article = st.text_area("Paste your article here:")

# Summarization button
if st.button("Summarize"):
    if article:
        # Perform summarization
        result = summarizer(article, max_length=1000, min_length=30, do_sample=False)
        
        # Display the summary
        st.subheader("Summary:")
        st.write(result[0]["summary_text"])
    else:
        st.warning("Please enter an article for summarization.")

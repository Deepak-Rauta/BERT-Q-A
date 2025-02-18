import streamlit as st
from transformers import pipeline

# Load a lightweight DistilBERT model for Q&A
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Streamlit UI
st.title("BERT Question Answering App 🤖")
st.write("Enter a **context** and ask a **question** to get an answer.")

# Input fields
context = st.text_area("Enter Context:", height=200)
question = st.text_input("Enter Question:")

# Answer Button
if st.button("Get Answer"):
    if context and question:
        # Get the answer from BERT
        result = qa_pipeline(question=question, context=context)
        st.subheader("Answer:")
        st.write(result['answer'])
    else:
        st.warning("Please enter both context and question.")

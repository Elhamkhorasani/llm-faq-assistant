import streamlit as st
from utils import answer_question

st.title("LLM-Powered FAQ Assistant 🚗")
question = st.text_input("Ask your question:")
if st.button("Get Answer"):
    if question:
        with st.spinner("Thinking..."):
            answer = answer_question(question)
            st.success(answer)

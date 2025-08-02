import streamlit as st

# Import the RAG system
from backend_rag import rag_system

st.title("Legal Decision Support System")
st.write("Ask questions about the content of constitution.pdf")
st.write("**Disclaimer**: This is an AI-based Retrieval-Augmented Generation (RAG) model trained on the Sri Lankan Constitution (Revised Edition – 2023). Answers are generated based on the document and may not reflect official legal advice. Use at your own discretion.")

# Input text box for the question
question = st.text_input("Enter your question here")

# Button to submit the question
if st.button("Get Answer"):
    if question:
        with st.spinner("Processing your question..."):
            answer = rag_system.answer_question(question)
            st.text_area("Answer", value=answer, height=200)
    else:
        st.write("Please enter a question!")

# Optional: Add some instructions
st.write("Example questions: 'What is the voting age?' or 'What are the emergency powers?'")
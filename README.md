# Legal Decision Support System

This is an AI-based Retrieval-Augmented Generation (RAG) application designed to answer questions about the Sri Lankan Constitution. The app uses a combination of natural language processing and document retrieval to provide insights based on the `constitution.pdf` file.

## Features
- Answers questions based on the content of the Sri Lankan Constitution.
- Simple Streamlit interface for user interaction.
- Powered by LangChain, Hugging Face models, and Chroma vector store.

## Prerequisites
- Python 3.8 or higher
- Internet connection (for initial model download)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dhananjayaDev/legal_decision_support_system.git
   cd legal_dss_app
   ```
2. Create a virtual environment and activate it:
   - Linux/Mac: `python -m venv venv && source venv/bin/activate`
   - Windows: `python -m venv venv && venv\Scripts\activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure `constitution.pdf` is in the project directory.

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your browser and go to `http://localhost:8501`.
3. Enter a question (e.g., "What is the voting age?") and click "Get Answer" to see the response.

## Disclaimer
This is an AI-based model trained on the Sri Lankan Constitution. The answers provided are for informational purposes only and should not be considered official legal advice. Use the system at your own discretion.

## File Structure
```
legal_dss_app/
├── backend_rag.py        # RAG logic and PDF processing
├── app.py               # Streamlit app interface
├── constitution.pdf      # Input PDF file
├── requirements.txt      # Dependency list
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Issues and suggestions are welcome!

## License
[(https://github.com/dhananjayaDev/legal_decision_support_system?tab=MIT-1-ov-file#readme)] MIT License.

## Acknowledgments
- Built using LangChain, Hugging Face, Chroma, and Streamlit.
- Inspired by the legal decision support system notebook.


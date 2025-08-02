import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

class RAGSystem:
    def __init__(self, pdf_path='constitution.pdf'):
        self.pdf_path = pdf_path
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.llm = self._setup_llm()
        self.retriever = self._setup_retriever()

    def _load_pdf(self):
        with open(self.pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
        return text

    def _setup_retriever(self):
        pdf_text = self._load_pdf()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_text(pdf_text)
        db = Chroma.from_texts(texts=chunks, embedding=self.embeddings)
        return db.as_retriever(search_kwargs={"k": 5})

    def _setup_llm(self):
        model_id = "google/flan-t5-base"
        text_gen_pipeline = pipeline("text2text-generation", model=model_id, max_length=512)
        return HuggingFacePipeline(pipeline=text_gen_pipeline)

    def answer_question(self, query):
        from langchain.chains import RetrievalQA
        qa = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=self.retriever)
        return qa.run(query)

# Instantiate the RAG system for use in the app
rag_system = RAGSystem()
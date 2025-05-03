from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_community.llms import HuggingFacePipeline
from dotenv import load_dotenv
from src.prompt import *
import os
import torch

app = Flask(__name__)

# Load environment variables from .env
load_dotenv()

# Load DeepSeek model locally or from Hugging Face Hub
model_name = "deepseek-ai/deepseek-llm-7b-chat"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

# HuggingFace pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    temperature=0.4,
    top_p=0.95,
    repetition_penalty=1.1
)

llm = HuggingFacePipeline(pipeline=pipe)

# Embeddings
embeddings = download_hugging_face_embeddings()

# Pinecone vector index
index_name = "nilecare"

# Load Pinecone vector store
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Prompt setup
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# Combine into retrieval-augmented generation chain
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Routes
@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print("User input:", msg)
    response = rag_chain.invoke({"input": msg})
    print("Response:", response["answer"])
    return str(response["answer"])

@app.route("/healthz")
def healthz():
    return "ok", 200

# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

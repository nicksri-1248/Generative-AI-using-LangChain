# from langchain_huggingface import ChatHuggingFace, HuggingFaceHub
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # repo_id="HuggingFaceH4/zephyr-7b-beta",
    # repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    repo_id="moonshotai/Kimi-K2-Instruct-0905",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("What is the capital of India?")

print(result.content)
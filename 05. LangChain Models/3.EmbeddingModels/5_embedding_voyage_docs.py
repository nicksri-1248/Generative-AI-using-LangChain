from langchain_voyageai import VoyageAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = VoyageAIEmbeddings(model="voyage-3-large", output_dimension=256)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

result = embeddings.embed_documents(documents)

print(str(result))
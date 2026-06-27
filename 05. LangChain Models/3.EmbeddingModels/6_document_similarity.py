# from langchain_voyageai import VoyageAIEmbeddings
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
# from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# load_dotenv()

# embeddings = VoyageAIEmbeddings(model="voyage-3-large", output_dimension=300)
# embeddings = VoyageAIEmbeddings(model="voyage-3-large", output_dimension=256)
# embeddings = GoogleGenerativeAIEmbeddings(model = "gemini-embedding-001", dimensions = 300)
embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# query = 'tell me about virat kohli'
query = 'tell me about bumrah'

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key = lambda x: x[1])[-1]

print(query)
print(documents[index])
print("similarity score is: ", score)
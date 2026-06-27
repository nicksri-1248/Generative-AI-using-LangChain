from langchain_voyageai import VoyageAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# embeddings = VoyageAIEmbeddings(model="voyage-3", dimensions=32)
embeddings = VoyageAIEmbeddings(model="voyage-3-large", output_dimension=256)
# embeddings = VoyageAIEmbeddings(model="voyage-3")

result = embeddings.embed_query("Delhi is the capital of India")

print(str(result))
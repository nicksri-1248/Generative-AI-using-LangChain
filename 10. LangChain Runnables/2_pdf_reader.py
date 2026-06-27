# # from langchain.document_loaders import TextLoader
# # from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_core.vectorstores import FAISS
# from langchain_anthropic import AnthropicLLM

# # Load the document
# loader = TextLoader("docs.txt")     # Ensure docs.txt exists
# documents = loader.load()

# # Split the text into smaller chunks
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
# docs = text_splitter.split_documents(documents)

# # Convert text into embeddings & store in FAISS
# vectorstore = FAISS.from_documents(docs, GoogleGenerativeAIEmbeddings())

# # Create a retiever (fetches relevant documents)
# retriever = vectorstore.as_retriever()

# # Manually Retrieve Relevant Documents
# query = "What are the key takeaways from the document?"
# retrieved_docs = retriever.get_relevant_documents(query)

# # Combine Retrieved Text into a Single Prompt
# retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])

# # Initialize the LLM
# llm = AnthropicLLM(model="claude-haiku-4-5-20251001", temperature=0.7)

# # Manually Pass Retrieved Text to LLM
# prompt = f"Based on the text, answer the following question: {query}\n\n{retrieved_text}"
# answer = llm.predict(prompt)

# # Print the Answer
# print("Answer:", answer)
# # from langchain.document_loaders import TextLoader
# # from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.document_loaders import TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_core.vectorstores import FAISS
# from langchain_anthropic import AnthropicLLM
# from langchain.chains import RetrievalQA

# # Load the document
# loader = TextLoader("docs.txt")     # Ensure docs.txt exists
# documents = loader.load()

# # Split the text into smaller chunks
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
# docs = text_splitter.split_documents(documents)

# # Convert text into embeddings & store in FAISS (Vector DB)
# vectorstore = FAISS.from_documents(docs, GoogleGenerativeAIEmbeddings())

# # Create a retiever (this fetches relevant documents)
# retriever = vectorstore.as_retriever()

# # Initialize LLM
# llm = AnthropicLLM(model="claude-haiku-4-5-20251001", temperature=0.7)

# # Create RetrievalQAChain
# qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# # Ask a question
# query = "What are the key takeaways from the document?"
# answer = qa_chain.run(query)

# print("Answer:", answer)
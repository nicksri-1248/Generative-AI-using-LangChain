from langchain_community.document_loaders import TextLoader
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-haiku-4-5-20251001")

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf8')

docs = loader.load()

print(docs)
print(type(docs))

print(len(docs))

print(docs[0])
print(type(docs[0]))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem': docs[0].page_content}))
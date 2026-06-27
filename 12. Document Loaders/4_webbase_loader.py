from langchain_community.document_loaders import TextLoader, WebBaseLoader
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-haiku-4-5-20251001")

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question', 'text']
)
    


parser = StrOutputParser()

url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
loader = WebBaseLoader(url)

docs = loader.load()

# print(len(docs))

# print(docs[0].page_content)

chain = prompt | model | parser

print(chain.invoke({'question': 'What is the product we are talking about?', 'text': docs[0].page_content}))

# Project Idea

# Chrome Plugin where user can chat with LLM about the content of the webpage they are currently on. The plugin will extract the text from the webpage and send it to the LLM for processing. The user can then ask questions about the content of the webpage and get answers from the LLM.
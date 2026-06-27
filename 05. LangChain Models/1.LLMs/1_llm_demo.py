from langchain_anthropic import AnthropicLLM
from dotenv import load_dotenv

load_dotenv()

llm = AnthropicLLM(model="claude-haiku-4-5-20251001")

result = llm.invoke("What is the capital of India")

print(result)
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatAnthropic(model="claude-haiku-4-5-20251001")

print(model.get_input_jsonschema())
print(model.get_output_jsonschema())


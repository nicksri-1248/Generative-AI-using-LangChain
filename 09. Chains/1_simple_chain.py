from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 intresting facts about {topic}.',
    input_variables=['topic']
)

model = ChatAnthropic(model = "claude-haiku-4-5-20251001")

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'cricket'})

print(result)

chain.get_graph().print_ascii()
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatAnthropic(model = "claude-haiku-4-5-20251001")

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instructions}',
    input_variables = ['feedback'],
    partial_variables = {'format_instructions': parser2.get_format_instructions()}
)

# classifier_chain = prompt1 | model | parser
classifier_chain = prompt1 | model | parser2

# print(classifier_chain.invoke({'feedback': 'This is a terrible smartphone'}).sentiment)
# print(classifier_chain.invoke({'feedback': 'This is a wonderful smartphone'}).sentiment)

# result = classifier_chain.invoke({'feedback': 'This is a wonderful smartphone'}).sentiment
# result = classifier_chain.invoke({'feedback': 'This is a terrible smartphone'}).sentiment

# print(result)

prompt2 = PromptTemplate(
    template = 'Write an appropriate response to this positive feedback \n {feedback}',
    input_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = 'Write an appropriate response to this negative feedback \n {feedback}',
    input_variables = ['feedback']
)

# branch_chain = RunnableBranch(
#     (condition1, chain1),
#     (condition2, chain2),
#     default_chain
# )

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

# print(chain.invoke({'feedback': 'This is a terrible phone'}))
print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()
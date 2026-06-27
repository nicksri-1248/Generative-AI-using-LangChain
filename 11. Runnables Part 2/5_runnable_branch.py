from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a detailed report {topic}.',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Summarize the following text \n {text}.',
    input_variables = ['text']
)

model = ChatAnthropic(model = "claude-haiku-4-5-20251001")

parser = StrOutputParser()

# report_gen_chain = RunnableSequence(prompt1, model, parser)

report_gen_chain = prompt1 | model | parser

# branch_chain = RunnableBranch(
#     (condition, runnable),
#     default
# )

branch_chain = RunnableBranch(
    # (lambda x: len(x.split()) > 500, RunnableSequence(prompt2, model, parser)),
    # (lambda x: len(x.split()) > 300, RunnableSequence(prompt2, model, parser)),
    (lambda x: len(x.split()) > 300, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic': 'Russia vs Ukraine'}))
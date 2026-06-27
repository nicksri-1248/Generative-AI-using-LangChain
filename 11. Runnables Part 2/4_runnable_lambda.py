# from langchain_core.runnables import RunnableLambda

# def word_counter(text):
#     return len(text.split())

# runnable_word_counter = RunnableLambda(word_counter)

# print(runnable_word_counter.invoke('Hi there how are you?'))

from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel

load_dotenv()

def word_counter(text):
    return len(text.split())

prompt = PromptTemplate(
    template = 'Write a joke about {topic}.',
    input_variables = ['topic'],
)

model = ChatAnthropic(model = "claude-haiku-4-5-20251001")

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_counter),
})

# parallel_chain = RunnableParallel({
#     'joke': RunnablePassthrough(),
#     'word_count': RunnableLambda(lambda x: len(x.split()))
# })

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# print(final_chain.invoke({'topic': 'AI'}))

result = final_chain.invoke({'topic': 'AI'})

final_result = """{} \n word count: {}""".format(result['joke'], result['word_count'])

print(final_result)
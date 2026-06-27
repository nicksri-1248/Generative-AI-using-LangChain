# from langchain_anthropic import AnthropicLLM
# # from langchain_core.chains import LLMChain
# from langchain_core.prompts import PromptTemplate

# # Load the LLM (Haiku-4.5)
# llm = AnthropicLLM(model="claude-haiku-4-5-20251001", temperature=0.7)

# # Create a prompt template
# prompt = PromptTemplate(
#     input_variables=["topic"],
#     template="Suggest a catchy blog title about {topic}."
# )

# # Create an LLMChain
# chain = LLMChain(llm=llm, prompt=prompt)

# # Run the chain with a specific topic
# topic = input('Enter a topic')
# output = chain.run(topic)

# print("Generated Blog Title:", output)
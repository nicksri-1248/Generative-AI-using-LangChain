# from langchain.llms import OpenAI
from langchain_anthropic import AnthropicLLM
from langchain_core.prompts import PromptTemplate

# Initialize the LLM
llm = AnthropicLLM(model="claude-haiku-4-5-20251001", temperature=0.7)

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}."
)

# Define the input
topic = input('Enter a topic')

# Format the prompt manually using PromptTemplate
formatted_prompt = prompt_template.format(topic=topic)

# Call the LLM directly
blog_title = llm.predict(formatted_prompt)

# Print the output
print("Generated Blog Title:", blog_title)
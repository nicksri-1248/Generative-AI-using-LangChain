# from langchain_sarvam import ChatSarvam
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatSarvam(model="sarvam-30b")

# result = model.invoke("What is the capital of India?")
# # result = model.invoke("भारत की राजधानी क्या है?")
# print(result)

# from langchain_sarvam import ChatSarvam
from langchain_sarvamcloud import ChatSarvam
from dotenv import load_dotenv

load_dotenv()

model = ChatSarvam(model="sarvam-105b")
# model.model_kwargs = {"model": "sarvam-30b"}  # workaround for langchain_sarvam bug

result = model.invoke("What is the capital of India?")
# print(result)
print(result.content)
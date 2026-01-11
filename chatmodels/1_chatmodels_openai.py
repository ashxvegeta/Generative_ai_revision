from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
# max_completion_tokens = the maximum number of tokens the model is allowed to generate in the response
# Tokens ≠ words (a token can be a word or part of a word)
# This limits the length of the AI’s answer
model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0,max_completion_tokens=10)
result = model.invoke("Explain the causes of World War II?")
print(result.content)
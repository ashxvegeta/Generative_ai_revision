from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0,max_completion_tokens=10)
result = model.invoke("Explain the causes of World War II?")
print(result.content)
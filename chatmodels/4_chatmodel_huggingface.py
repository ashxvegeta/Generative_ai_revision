from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=256,
)

model =ChatHuggingFace(llm=llm)
response = model.invoke("Explain the theory of relativity in simple terms.")
print(response.content)

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
chat_model = ChatGoogleGenerativeAI(model= "gemini-2.5-flash")

prompt = "what is capital of USA?"
chat_model_response = chat_model.invoke(prompt)
print(chat_model_response)
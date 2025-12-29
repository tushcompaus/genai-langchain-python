from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

import os

load_dotenv()
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
chat_model = ChatGoogleGenerativeAI(model= "gemini-2.5-flash")

chat_history =[SystemMessage(content = "Yoy are an AI Assistant")]

while True :
    user_input = input("YOU:")
    if user_input == "exit":
        break
    chat_history.append(HumanMessage(content=user_input))
    chat_model_response = chat_model.invoke(chat_history)
    chat_history.append(AIMessage(content=chat_model_response.content))
    print(chat_model_response.content)

print(f"FULL CHAT HISTORY: {chat_history}")
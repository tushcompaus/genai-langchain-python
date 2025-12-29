from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GEMINI_API_KEY"]= os.getenv("GEMINI_API_KEY")
chat_model = GoogleGenerativeAI(model="gemini-2.5-flash")

chat_prompt_template = ChatPromptTemplate(
        [
            ("system", "You are a expert {skill}"),
            ("human", "what is the definition of {term}"),
        ]
    )

prompt = chat_prompt_template.invoke({"skill":"doctor", "term":"cancer"})
print(f"PROMPT: {prompt}")
result = chat_model.invoke(prompt)
print(result)

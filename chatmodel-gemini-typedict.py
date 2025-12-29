from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GEMINI_API_KEY"]= os.getenv("GEMINI_API_KEY")

class review(TypedDict):
    sentiment:str
    summary:str

prompt = "i dont like my mobile , it always hangs when i play games on it"
model = ChatGoogleGenerativeAI(model ="gemini-2.5-flash")
model_typedict = model.with_structured_output(review)
result = model_typedict.invoke(prompt)
print(result)
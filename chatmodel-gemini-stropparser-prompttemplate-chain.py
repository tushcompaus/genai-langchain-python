from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
from langchain_core.output_parsers import StrOutputParser

chat_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
template1 = PromptTemplate(template = "write a detailed report on {topic}",input_variables=['topic'])
template2 = PromptTemplate(template= "provide key takeways from {text}", input_variables=['text'])
parser = StrOutputParser()
chain = template1 | chat_model | parser | template2 | chat_model | parser
result = chain.invoke({"topic":"generative ai"})
print(result)
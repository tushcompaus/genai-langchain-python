from typing import TypedDict, Annotated, Optional, Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GEMINI_API_KEY"]= os.getenv("GEMINI_API_KEY")


class review(BaseModel):
    sentiment : Literal["Positive", "Negative"] = Field(description="provide snetiment")
    key_terms : list[str] = Field(description= "provide key terms in the review", max_length=4)
    positive_things: list[str] = Field(description="provide positive apsects in review", max_length=4)
    negative_things : list[str]= Field(description="provide negative apsects in review",max_length=4)
    product_type: Literal["Mobile", "Game"] = Field(description="provide product type " )

prompt = """
It’s far from being “too little, too late” for this venerable battle royale to go free-to-play. PlayerUnknown’s Battlegrounds may be a known quantity these days, but its slower paced survival of the fittest struggle still creates memorable shootouts and intense moments in nearly every match. However, console players might find its efforts to render its massive 8x8 km maps in proper detail technically disappointing, and no matter where you play its vehicles are no joyride. Thankfully, PUBG has plenty of life left in it if you can look past the clunky weapons and vehicles to see the much more hectic firefights and interesting, tactics-focused survival that house them.
"""
model = ChatGoogleGenerativeAI(model ="gemini-2.5-flash")
model_typedict = model.with_structured_output(review)
result = model_typedict.invoke(prompt)
print(result)
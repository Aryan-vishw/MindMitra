from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

def analyze_mood(user_input: str) -> str:
    llm = ChatOpenAI(
        model="gpt-4",  # or use "gpt-3.5-turbo" if you're on the free tier
        temperature=0.7,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    prompt = PromptTemplate(
        input_variables=["input"],
        template="""
You are a professional mood analysis system.

Analyze the following user's input and identify their emotional state.
From the following list, choose the most relevant emotions (one or more): 
Happy, Sad, Angry, Anxious, Stressed, Excited, Content, Irritable, Calm, Energetic,
Tired, Frustrated, Overwhelmed, Relaxed, Optimistic, Pessimistic, Lonely, Loved, Bored, Motivated.

Input:
"{input}"

Respond with:
- Detected Emotion(s): <comma-separated emotions>
- Reasoning: <brief reasoning based on input>
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(input=user_input)
    return result

from langchain.agents import Tool, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI  # ✅ Switched from Google to OpenAI
from tools.mood_analysis_tool import analyze_mood
from tools.coping_tool import suggest_coping
import os


def get_mindmitra_agent():
    llm = ChatOpenAI(
        model="gpt-4",  # You can also try "gpt-3.5-turbo"
        temperature=0.3,
        openai_api_key=os.getenv("OPENAI_API_KEY")  # ✅ Uses OpenAI key
    )

    tools = [
        Tool(
            name="MoodAnalyzer",
            func=analyze_mood,
            description="Analyzes the user's emotional tone and returns the detected emotion(s)."
        ),
        Tool(
            name="CopingAdvisor",
            func=suggest_coping,
            description="Provides personalized strategies to cope with the user's current emotional state."
        ),
    ]

    system_message = (
        "You are MindMitra, a compassionate AI mental wellness companion. "
        "You listen, reflect, and support users with emotional insights. "
        "Always validate their feelings and offer non-judgmental advice. "
        "If they seem low, provide calming suggestions. If they are positive, help them maintain momentum."
    )

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        agent_kwargs={"system_message": system_message}
    )

    return agent

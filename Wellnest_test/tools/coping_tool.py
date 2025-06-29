from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

def suggest_coping(emotion_input: str) -> str:
    prompt = PromptTemplate(
        input_variables=["emotion"],
        template="""
You are a wellness companion who provides actionable and empathetic strategies based on the user's emotional state.

Emotion Detected: {emotion}

Give 2–3 practical suggestions the user can try. Format it as:
- 💡 Tip 1
- 💡 Tip 2
- 💡 Tip 3 (if needed)

Keep your tone positive and supportive. Avoid generic advice. Base tips on evidence-backed self-care or cognitive-behavioral practices when possible.
"""
    )

    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        raise ValueError("OPENAI_API_KEY is not set in environment variables.")

    llm = ChatOpenAI(
        temperature=0.4,
        model="gpt-4",
        openai_api_key=openai_key,
    )


    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(emotion=emotion_input)
    return result

import streamlit as st
from agents.mood_store import get_mindmitra_agent
from memory.memory_store import get_last_mood, set_last_mood
from ui.layout import show_header, show_footer, show_about_expander, show_quote

st.set_page_config(page_title="MindMitra", page_icon="🧠", layout="centered")

# ========== Header ==========
show_header()
show_quote()
show_about_expander()
st.markdown("---")

# ========== Load Agent ==========
agent = get_mindmitra_agent()

# ========== User Input ==========
st.subheader("How are you feeling today?")
user_input = st.text_area("Share what's on your mind:", placeholder="e.g. I feel anxious about my work and tired all the time...")

# ========== Wake Up Agent Button ==========
if st.button("👋 Wake Up Your Agent"):
    last_mood = get_last_mood()
    if last_mood:
        st.success(f"Welcome back! Last time you felt **{last_mood}**. Would you like to talk more about it?")
    else:
        st.info("Hi, I'm MindMitra. How are you feeling today? You can share anything — I'm here to help.")

# ========== Analyze Button ==========
if st.button("🧠 Analyze My Mood"):
    if user_input.strip() == "":
        st.warning("Please enter some text before analyzing.")
    else:
        with st.spinner("Analyzing your emotions..."):
            response = agent.run(user_input)
            st.markdown("### 🤖 MindMitra Says:")
            st.markdown(response)

            # Extract primary mood from response if possible
            if "Detected Emotion(s):" in response:
                start = response.find("Detected Emotion(s):") + len("Detected Emotion(s):")
                mood_text = response[start:].split("\n")[0].strip()
                set_last_mood(mood_text)
            else:
                set_last_mood("Unknown")

# ========== Footer ==========
show_footer()

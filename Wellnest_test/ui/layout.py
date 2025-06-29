import streamlit as st
from PIL import Image

def show_header():
    logo_path = "assets/logo.png"  # Ensure your logo is here
    try:
        image = Image.open(logo_path)
        st.image(image, width=120)
    except:
        st.title("🧠 MindMitra")

    st.markdown("<h2 style='color: #4B8BBE;'>Your AI-powered mental wellness companion</h2>", unsafe_allow_html=True)
    st.write("Take a moment. Reflect. Let’s talk.")

def show_footer():
    st.markdown("---")
    st.markdown(
        "Built with ❤️ by Team MindMitra | [Website](https://www.lyzr.ai/) | [Discord](https://discord.gg/nm7zSyEFA2)"
    )

def show_about_expander():
    with st.expander("ℹ️ About MindMitra"):
        st.write("""
        MindMitra is an AI-powered agent designed to support your mental wellness.
        It listens to your feelings, analyzes your emotional state, and offers personalized advice
        using evidence-based techniques and positive reinforcement.
        """)

def show_quote():
    # Optional: Use API here instead
    quote = "“You don't have to control your thoughts. You just have to stop letting them control you.” — Dan Millman"
    st.markdown(f"> 💬 *{quote}*")

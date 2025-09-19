"""
Plant Disease Focused Chatbot using Groq AI
"""
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

def ask_groq(prompt: str) -> str:
    """Ask Groq AI specifically about plant diseases and care"""
    try:
        # Load environment - try Streamlit secrets first, then .env file
        api_key = None
        
        # For Streamlit Cloud deployment
        if hasattr(st, 'secrets') and 'GROQ_API_KEY' in st.secrets:
            api_key = st.secrets["GROQ_API_KEY"]
        else:
            # For local development
            env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
            load_dotenv(env_path)
            api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            return "⚠️ Error: GROQ_API_KEY not found in environment or Streamlit secrets."
        
        # Create a plant-focused system prompt
        system_prompt = """You are a plant disease expert and agricultural specialist. 
        Always respond in English about plant diseases, plant care, gardening, and agriculture topics only.
        Provide practical, scientific advice about:
        - Plant disease identification and treatment
        - Disease prevention methods
        - Plant care and maintenance
        - Organic and chemical treatment options
        - Environmental factors affecting plant health
        
        If asked about non-plant topics, politely redirect to plant-related topics.
        Keep responses helpful, accurate, and focused on plant health."""
        
        # Create client and get response
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"⚠️ Error connecting to plant disease expert: {str(e)[:100]}..."


def test_connection():
    """Test the chatbot"""
    return ask_groq("What are common tomato plant diseases?")

import streamlit as st
import torch
import warnings
from utils.preprocess import preprocess_image
from utils.predict import load_model, predict
from utils.chatbot import ask_groq

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore", category=UserWarning)

# ------------------------------
# Streamlit page configuration
# ------------------------------
st.set_page_config(page_title="🌱 Plant Disease Detector + Chatbot", layout="wide")

# ------------------------------
# Load Model (cached to avoid reloading)
# ------------------------------
@st.cache_resource
def load_trained_model():
    try:
        model, class_names = load_model("models/best_plant_model.pth")
        return model, class_names
    except FileNotFoundError:
        st.error("⚠️ Model file not found! Please place 'best_plant_model.pth' in the 'models/' folder.")
        return None, None
    except Exception as e:
        st.error(f"⚠️ Error loading model: {str(e)}")
        return None, None

# Try to load model
model, class_names = load_trained_model()

# ------------------------------
# UI - Title
# ------------------------------
st.title("🌱 Plant Disease Detection & Plant Health Chatbot")
st.write("Upload a leaf image to detect plant diseases, and chat with AI for remedies & tips.")

# ------------------------------
# Section 1: Image Upload + Prediction
# ------------------------------
uploaded_file = st.file_uploader("📤 Upload a plant leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Leaf", width='stretch')
    
    if model is None or class_names is None:
        st.error("❌ Cannot make predictions without a trained model. Please add your model file first.")
        st.info("💡 Place your 'plant_disease_model.pth' file in the 'models/' folder and refresh the page.")
    else:
        # Preprocess image
        image_tensor = preprocess_image(uploaded_file)

        # Run prediction
        predicted_class, confidence = predict(model, image_tensor, class_names)

        # Show results
        st.subheader("🔍 Prediction Result")
        st.success(f"Predicted Disease: **{predicted_class}** with confidence {confidence:.2f}%")
        
        # Store predicted disease in session state for chatbot context
        st.session_state.predicted_disease = predicted_class

        # Optional: automatically ask Groq for explanation
        with st.expander("💡 Learn more about this disease"):
            query = f"The detected plant disease is {predicted_class}. Explain its causes, symptoms, and prevention in simple terms."
            answer = ask_groq(query)
            st.write(answer)

# ------------------------------
# Section 2: Chatbot
# ------------------------------
st.subheader("🤖 Plant Health Chatbot")
if hasattr(st.session_state, 'predicted_disease') and st.session_state.predicted_disease:
    st.write(f"💡 **Current Disease Context:** {st.session_state.predicted_disease}")
    st.write("Ask about this disease or any other plant care topics!")
else:
    st.write("Ask anything about plant care, disease prevention, or remedies!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if user_input := st.chat_input("Ask me anything about plants..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Create context-aware query
    if hasattr(st.session_state, 'predicted_disease') and st.session_state.predicted_disease:
        # If there's a predicted disease and user asks about "this/that disease", provide context
        if any(word in user_input.lower() for word in ['this disease', 'that disease', 'the disease', 'about it', 'more about']):
            context_query = f"The user is asking about {st.session_state.predicted_disease} (recently predicted plant disease). User question: {user_input}"
            response = ask_groq(context_query)
        else:
            # Regular plant question with disease context available
            context_query = f"Context: Recently detected plant disease is {st.session_state.predicted_disease}. User question: {user_input}"
            response = ask_groq(context_query)
    else:
        # No disease prediction context
        response = ask_groq(user_input)

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})

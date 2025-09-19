# 🌱 Plant Disease Detection & AI Chatbot

A comprehensive Streamlit web application that combines deep learning-based plant disease detection with an AI-powered chatbot for plant care advice.

## ✨ Features

- **🔍 Plant Disease Detection**: Upload plant leaf images for AI-powered disease classification
- **🤖 Intelligent Chatbot**: Get expert advice on plant diseases, care, and prevention
- **📊 Confidence Scores**: Receive prediction confidence levels
- **💡 Disease Information**: Detailed explanations of detected diseases
- **🎯 Plant-Focused AI**: Specialized responses for agricultural and gardening topics

## 🚀 Live Demo

[Deploy to Streamlit Cloud](https://streamlit.io/cloud)

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Deep Learning**: PyTorch, TorchVision
- **AI Chat**: Groq LLama 3.1
- **Image Processing**: PIL/Pillow
- **Model Architecture**: EfficientNet-B2 with custom classifier

## 📁 Project Structure

```
plant-disease-streamlit/
├── app.py                    # Main Streamlit application
├── models/
│   └── best_plant_model.pth  # Trained PyTorch model
├── utils/
│   ├── preprocess.py         # Image preprocessing
│   ├── predict.py           # Model inference
│   └── chatbot.py           # AI chatbot integration
├── requirements.txt          # Dependencies
├── .env                     # Environment variables (local)
├── .streamlit/
│   └── secrets.toml         # Streamlit Cloud secrets
└── README.md

```

## 🔧 Setup & Installation

### Local Development

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd plant-disease-streamlit
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

5. **Run the application**
```bash
streamlit run app.py
```

### Streamlit Cloud Deployment

1. **Fork this repository** to your GitHub account

2. **Get your Groq API Key**
   - Visit [Groq Console](https://console.groq.com/)
   - Create an account and generate an API key

3. **Deploy to Streamlit Cloud**
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Connect your GitHub account
   - Select this repository
   - Set up secrets in the deployment settings:
     ```
     GROQ_API_KEY = "your_groq_api_key_here"
     ```

4. **Deploy!** 🚀

## 🎯 Usage

1. **Disease Detection**:
   - Upload a clear image of a plant leaf
   - Get instant disease classification with confidence scores
   - View detailed disease information and treatment advice

2. **AI Chatbot**:
   - Ask questions about plant diseases, care, or prevention
   - Get expert-level responses focused on agriculture and gardening
   - Learn about organic and chemical treatment options

## 🔑 Environment Variables

- `GROQ_API_KEY`: Your Groq API key for AI chatbot functionality

## 📋 Requirements

See `requirements.txt` for full dependency list:
- streamlit==1.49.1
- torch==2.8.0
- torchvision==0.23.0
- pillow==11.3.0
- python-dotenv==1.1.1
- groq==0.31.1

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Groq](https://groq.com/) AI
- Deep learning with [PyTorch](https://pytorch.org/)

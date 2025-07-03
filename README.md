# GenAI
Features
1. Uses LangChain to manage prompt templates and chaining.
2. Integrates Ollama with the LLaMA2 model for local inference.
3. Uses Streamlit for a clean and interactive UI.
4. Loads environment variables securely using python-dotenv.



Requirements
Install the following Python packages:
pip install langchain_openai langchain_core langchain_community python-dotenv streamlit fastapi langserve uvicorn sse_starlette



Product Structure
├── app.py               # Main Streamlit app
├── .env                 # Environment variables (e.g., OPENAI_API_KEY)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation



Environment Variables
Create a .env file in the root directory and add your OpenAI API key:

OPENAI_API_KEY = API_KEY



Running the App

streamlit run app.py

# Langchain-M1-Youtube-Parser

A collection of LangChain-powered applications demonstrating AI capabilities with Groq's Llama 3 model.

## Features

This repository contains two main applications:

### 1. Pet Name Generator
- Interactive Streamlit web application
- Generates creative pet names based on animal type and color
- Uses Groq's Llama 3-70B model for name suggestions
- Supports multiple pet types: Cat, Dog, Cow, Hen, Hamster

### 2. YouTube Assistant
- Streamlit application for YouTube video analysis
- Extracts and processes video transcripts
- Uses vector embeddings (FAISS) for semantic search
- Answers questions about video content using RAG (Retrieval-Augmented Generation)
- Powered by Groq's Llama 3-70B model

## Prerequisites

- Python 3.8 or higher
- Groq API key (get one at [https://console.groq.com/](https://console.groq.com/))

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Langchain-M1-Youtube-Parser
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix/macOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install langchain langchain-groq langchain-community streamlit python-dotenv sentence-transformers
```

## Environment Setup

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

### Pet Name Generator

Run the application:
```bash
streamlit run main.py
```

**How to use:**
1. Select your pet type from the sidebar (Cat, Dog, Cow, Hen, or Hamster)
2. Enter the color of your pet
3. Click submit to receive 5 creative name suggestions

### YouTube Assistant

Run the application:
```bash
streamlit run Youtube_Assistance/YT_main.py
```

**How to use:**
1. Enter a YouTube video URL in the sidebar
2. Ask a question about the video content
3. Click submit to get an AI-powered answer based on the video transcript

**Note:** The first run will download the HuggingFace embeddings model (~100MB), which may take a few minutes.

## Project Structure

```
Langchain-M1-Youtube-Parser/
├── main.py                          # Pet name generator Streamlit app
├── langchain_helper.py              # Helper functions for pet name generator
├── Youtube_Assistance/
│   ├── YT_main.py                   # YouTube assistant Streamlit app
│   └── YT_langchain_helper.py       # Helper functions for YouTube video analysis
├── .env                             # Environment variables (not in git)
└── README.md                        # This file
```

## Dependencies

- `langchain` - LangChain framework
- `langchain-groq` - Groq integration for LangChain
- `langchain-community` - Community integrations (Wikipedia, YouTube loader)
- `streamlit` - Web application framework
- `python-dotenv` - Environment variable management
- `sentence-transformers` - HuggingFace embeddings
- `faiss-cpu` - Vector similarity search

## Technical Details

### Pet Name Generator
- Uses LangChain's Runnable interface for chain composition
- Implements prompt templates for structured inputs
- Temperature set to 0.7 for creative outputs

### YouTube Assistant
- Uses `YoutubeLoader` to extract video transcripts
- Implements `RecursiveCharacterTextSplitter` for chunking
- Uses FAISS vector store for efficient similarity search
- Implements RAG pattern for context-aware responses
- Temperature set to 0.7 for balanced responses

## License

This project is provided as-is for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

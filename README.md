# Overview

This project is an LLM-powered assistant that helps users understand garbage disposal classifications in Asaka City.

# Getting Started

Follow the steps below to set up and run the project.

1. Create a Virtual Environment

```bash
python3 -m venv venv
```

2. Activate the Virtual Environment

```bash
git clone https://github.com/yourusername/multimodal-chat.git
cd multimodal-chat
```

3. Install Dependencies
   Install the required libraries using:

```bash
pip install -r requirements.txt
```

4. Set Up the OpenAPI Key

```bash
export OPENAI_API_KEY=your_api_key_here
```

Other ways to do this include:

1. Use python-dotenv to manage environment variables.
2. Store the key as a secret in GitHub Actions.

3. Create the Index
   Run the following script to generate the index:

```bash
streamlit run multimodal_chat/app.py
```

6. Start the Chatbot

```bash
python asakaGomiSortChat.py
```

# Demo

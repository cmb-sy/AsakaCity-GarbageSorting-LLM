# Overview

This project is an LLM-powered assistant that helps users understand garbage disposal classifications in Asaka City.

# Getting Started

Follow the steps below to set up and run the project.

### 1. Create a Virtual Environment
```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the OpenAPI Key
You can set the OpenAPI key in one of the following ways:
```bash
export OPENAPI_KEY=your_openapi_key
```
Other ways to do this include:
1. Use python-dotenv to manage environment variables.
2. Store the key as a secret in GitHub Actions.

### 5. Create the Index
```bash
python makeIndex.py
```

### 6. Start the LLM
```bash
python asakaGomiSortChat.py
```

# Demo

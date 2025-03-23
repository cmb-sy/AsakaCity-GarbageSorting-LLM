# Overview

This project is an LLM-powered assistant that helps users understand garbage disposal classifications in Asaka City.

# Getting Started

Follow the steps below to set up and run the project.

1. Create a Virtual Environment
   Run the following command to create a virtual environment:

```bash
python3 -m venv venv
```

2. Activate the Virtual Environment
   Activate the virtual environment with:

```bash
source venv/bin/activate
```

3. Install Dependencies
   Install the required libraries using:

```bash
pip install -r requirements.txt
```

4. Set Up the OpenAPI Key
   You can set the OpenAPI key in one of the following ways:

```bash
export OPENAPI_KEY=your_openapi_key
```

5. Create the Index
   Run the following script to generate the index:

```bash
python makeIndex.py
```

6. Start the Chatbot
   Launch the LLM:

```bash
python asakaGomiSortChat.py
```

# Demo

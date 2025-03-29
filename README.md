# Multimodal Chat - Asaka City Garbage Disposal Assistant

## Overview

This project is an LLM-powered assistant that helps users understand garbage disposal classifications in Asaka City.

## Getting Started

Follow the steps below to set up and run the project.

### 1. Clone the Repository

```bash
git clone https://github.com/cmb-sy/AsakaCity-GarbageSorting-LLM.git
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

#### Linux/macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up the OpenAI API Key

```bash
export OPENAI_API_KEY=your_api_key_here
```

**Alternative Methods:**

- Use python-dotenv to manage environment variables
- Store the key as a secret in GitHub Actions

### 6. Create the Index

```bash
python create_index.py
```

### 7. Start the Chatbot

```bash
python run.py
```

## Demo
https://github.com/user-attachments/assets/53114e69-9fe4-490b-915b-f3b28cc30c15





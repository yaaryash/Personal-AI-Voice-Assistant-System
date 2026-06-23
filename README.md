# Multilingual AI Personal Voice Assistant

## Overview

A Python-based AI voice assistant that combines speech recognition, conversational AI, text-to-speech synthesis, and system automation. The assistant supports voice and text interactions, retrieves information from external sources, and performs various desktop automation tasks.

## Architecture

<img width="1536" height="1024" alt="Multilingual AI Architecture" src="https://github.com/user-attachments/assets/9ab53dff-0da7-4662-9cf5-0c265b19630a" />

The system consists of:

* Speech Recognition Engine
* Command Processing Layer
* Google Gemini AI Integration
* Text-to-Speech Engine
* Streamlit Web Interface
* Automation & Utility Modules
* Logging Framework

## Features

* Voice command recognition
* Multilingual interaction
* Conversational AI using Google Gemini
* Speech-to-Text conversion
* Text-to-Speech responses
* Wikipedia search
* Browser automation
* Music playback
* System application control
* Streamlit web interface
* Structured logging

## Technology Stack

* Python
* Streamlit
* Google Gemini API
* SpeechRecognition
* PyAudio
* pyttsx3
* gTTS
* Wikipedia API - In progress

## What I Learned

This project helped me gain practical experience in:

* Building end-to-end AI-powered applications
* Integrating Large Language Models (LLMs)
* Speech-to-Text and Text-to-Speech pipelines
* API integration and external service communication
* Streamlit web application development
* System automation using Python
* Modular software design and project organization
* Logging, debugging, and error handling

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Personal-AI-Voice-Assistant-System.git
cd Personal-AI-Voice-Assistant-System/Multilingual_AI_Assistant
```

### Create Virtual Environment

```bash
python -m venv 
```

### Activate Virtual Environment

Windows:
```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run main.py
```

## Future Improvements

* Memory and conversation history
* Wake-word detection
* Local LLM support
* Retrieval-Augmented Generation (RAG)
* Multi-agent architecture
* Docker deployment 


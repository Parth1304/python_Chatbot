# Python Chatbot Project

This project implements a simple chatbot in Python using Flask and integrates it with a machine learning model for generating responses.

## Features

- **Chatbot Interface**: Provides a web interface to interact with the chatbot.
- **Machine Learning Model**: Uses PyTorch for natural language processing tasks.
- **Deployment**: Deployed using Flask and Gunicorn for production-ready deployment.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd python_Chatbot

2. Set up a virtual environment (optional but recommended):
   ```bash
	python -m venv .venv
	. .venv/Scripts/activate  # On Windows
	source .venv/bin/activate  # On macOS/Linux
3. Install dependencies:

   ```bash
	pip install -r requirements.txt
	

## Usage

### Run the Flask application:

```bash
flask run

```
## Deployment

For deployment, it's recommended to use a WSGI server like Gunicorn. Example command to run with Gunicorn:

```bash
gunicorn -w 4 -b 127.0.0.1:5000 app:app

# Chatbot
AI Based Chatbot for Pdfs

### Requirements
    Flask
    google-generativeai
    pdfplumber
    werkzeug

## Installation

Flask PDF Chat Application
This is a Flask-based web application that allows users to chat with a Gemini AI model and upload PDF documents to provide context for the AI's responses.

Features
Interactive Chat: Engage in conversations with the Gemini AI.

PDF Contextualization: Upload PDF files, and the AI will use the document's content to answer your questions.

User Session Management: Maintains separate chat histories and PDF contexts for individual users.

Prerequisites
Before you begin, ensure you have the following installed:
Python 3.x: (Recommended Python 3.8 or higher)
pip: Python package installer (usually comes with Python)



Installation
Follow these steps to set up and run the application on your local machine.

1. Save the Code
Save your Flask application code (the one you provided) into a file named app.py in a directory of your choice.

2. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.
Open your terminal or command prompt.
Navigate to your project directory (where app.py is saved).
Create the virtual environment:

python -m venv venv
or python3 -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

3. Install Dependencies
With your virtual environment activated, install the required Python packages:

pip install Flask google-generativeai pdfplumber werkzeug

4. Set Up the uploads Directory
The application automatically creates an uploads directory in your project root to store uploaded PDF files. You don't need to create it manually.

Configuration
Gemini API Key: The application uses a hardcoded API key (AIzaSyD019Ag8GLoilSxvDJreiFSj8KToT85Jz8). For production environments, it's highly recommended to use environment variables or a more secure method to manage your API key.

Flask Secret Key: The app.secret_key is set to "your-secret-key". Change this to a strong, unique secret key for any deployment beyond local development.

Usage
Running the Application
A. From the Terminal
Ensure your virtual environment is active.

In your project directory, run:

python app.py

The Flask development server will start, typically on http://0.0.0.0:5050 or http://127.0.0.1:5050.


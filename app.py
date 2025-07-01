from flask import Flask, request, jsonify, session, send_file
import google.generativeai as genai
import pdfplumber
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "your-secret-key"
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

genai.configure(api_key="AIzaSyD019Ag8GLoilSxvDJreiFSj8KToT85Jz8")
model = genai.GenerativeModel('gemini-1.5-flash-latest')

chat_sessions = {}
pdf_context = {}  # Store PDF content per user

@app.route("/")
def home():
    return send_file("index.html")  # Changed from chat.html to index.html

@app.route("/ask", methods=["POST"])
def ask():
    user_id = session.get("user_id")
    if not user_id:
        user_id = str(id(session))
        session["user_id"] = user_id

    if user_id not in chat_sessions:
        chat_sessions[user_id] = model.start_chat(history=[])

    message = request.form["messageText"].strip()

    # Append PDF content if uploaded
    prompt = message
    if user_id in pdf_context:
        prompt = f"Answer using this document:\n\n{pdf_context[user_id]}\n\nUser question: {message}"

    try:
        chat = chat_sessions[user_id]
        response = chat.send_message(prompt)
        reply = response.text.strip()
    except Exception as e:
        reply = f"Error: {str(e)}"

    return jsonify({'status': 'OK', 'answer': reply})

@app.route("/upload", methods=["POST"])
def upload():
    user_id = session.get("user_id")
    if not user_id:
        user_id = str(id(session))
        session["user_id"] = user_id

    file = request.files["file"]
    if file and file.filename.endswith(".pdf"):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Extract text from PDF
        with pdfplumber.open(filepath) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)

        pdf_context[user_id] = text[:12000]  # Limit characters for Gemini context

        return jsonify({'status': 'OK', 'message': 'PDF uploaded and processed successfully.'})
    else:
        return jsonify({'status': 'ERROR', 'message': 'Only PDF files are supported.'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)

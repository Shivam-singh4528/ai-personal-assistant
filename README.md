# 🤖 AI Personal Assistant

### Your Intelligent Companion for Everyday Productivity

An AI-powered web application built with **Python, Flask, JavaScript, and the Groq API** that helps users get answers to their questions and summarize lengthy emails through a simple, interactive interface.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Groq_API-F55036?style=for-the-badge&logoColor=white" alt="Groq API"/>
</p>

---

## 📌 Overview

**AI Personal Assistant** is a web-based application designed to make everyday tasks easier using generative AI.

Whether you need a quick answer to a question or want to extract the key points from a long email, this application provides an easy way to interact with an AI model directly from your browser.

The project demonstrates practical implementation of AI API integration, backend development, frontend-backend communication, environment variable management, and asynchronous JavaScript.

## ✨ Features

### 💬 Ask Anything
- Ask questions in natural language.
- Receive AI-generated responses.
- View answers directly on the web page.

### 📧 Email Summarization
- Paste lengthy email content into the application.
- Generate concise summaries in approximately 2–3 sentences.
- Focus on the main purpose and important details of an email.

### ⚡ Interactive User Interface
- Simple and easy-to-use interface.
- Loading indicators while requests are processing.
- Display responses and error messages dynamically without reloading the page.

### 🔐 Secure Configuration
- Store API credentials in environment variables.
- Load configuration using `python-dotenv`.
- Keep sensitive credentials out of version control using `.gitignore`.

### 🧩 Flask Backend
- Separate endpoints for question answering and email summarization.
- JSON responses for frontend integration.
- Error handling for failed API requests.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework and API routes |
| HTML5 | Page structure |
| CSS3 | Styling and layout |
| JavaScript | Asynchronous requests and dynamic UI updates |
| Groq API | AI-powered text generation |
| python-dotenv | Environment variable management |
| Git & GitHub | Version control and project hosting |

## 🏗️ Project Architecture

```text
User
  |
  v
Web Interface (HTML + CSS)
  |
  v
JavaScript (Fetch API)
  |
  v
Flask Backend (main.py)
  |
  +---- /ask
  |
  +---- /summarize
  |
  v
Groq API
  |
  v
AI-Generated Response
  |
  v
Display Result in Browser
```

## 📂 Project Structure

```text
AIASSISTANT/
│
├── main.py                 # Flask application and API routes
├── templates/
│   └── index.html          # User interface and JavaScript
├── static/
│   └── style.css           # Application styling
├── .env                    # Private API credentials (not uploaded)
├── .gitignore              # Excludes secrets and temporary files
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd ai-personal-assistant
```

Replace `YOUR_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.env` file in the project root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from the [Groq Console](https://console.groq.com/).

**Security:** Never commit your real API key to GitHub or share it publicly.

### 5. Run the Application

```bash
python main.py
```

### 6. Open in Your Browser

Visit:

```text
http://127.0.0.1:5000
```

Your AI Personal Assistant is now ready to use!

## 🔄 How It Works

1. The user submits a question or email through the web interface.
2. JavaScript sends the form data to the relevant Flask endpoint.
3. Flask validates the input and sends a request to the Groq API.
4. The AI model generates a response or email summary.
5. Flask returns the result as JSON.
6. JavaScript displays the result on the page and manages the loading indicator.

## 🔒 Security & Best Practices

- Store API keys in `.env` rather than hardcoding them in Python files.
- Add `.env` to `.gitignore`.
- Do not expose API credentials in frontend JavaScript.
- Avoid committing virtual environments, cache files, or other unnecessary generated files.
- Be mindful of API usage limits and provider policies.

## 🔮 Future Enhancements

Potential improvements for future versions include:

- 🗂️ Chat history and conversation management
- 🎙️ Voice input and text-to-speech responses
- 📱 Improved responsive design for mobile devices
- 📄 Document summarization
- 🧠 Custom assistant personalities and prompts
- 💾 Persistent storage for user preferences
- 🌐 Deployment to a cloud hosting platform

*These are planned enhancements and may not be implemented in the current version.*

## 🎯 Learning Outcomes

Through this project, I practised:

- Building web applications using Flask.
- Integrating a third-party AI API.
- Connecting frontend and backend components.
- Handling asynchronous HTTP requests with JavaScript.
- Managing API credentials using environment variables.
- Implementing error handling and displaying dynamic responses.
- Organizing a Python project for version control.

## 👨‍💻 Author

**Shivam Singh**

B.Tech Information Technology | AI/ML Enthusiast

Interested in Artificial Intelligence, Machine Learning, and building practical AI-powered applications.

---

⭐ **If you find this project interesting, consider giving the repository a star!**

*Built as a hands-on project to explore AI integration and full-stack application development.*

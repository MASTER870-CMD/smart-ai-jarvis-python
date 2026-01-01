# 🎙️ Genius AI: The Ultra-Fast Multilingual Voice Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20UI-green?style=for-the-badge&logo=flask)
![Groq](https://img.shields.io/badge/Powered%20By-Groq%20LPU-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

> **Experience the world's fastest voice AI.** Combining the raw speed of Groq's LPU with a luxurious Gold & Cream Web UI, Genius AI speaks **English, Hindi, Kannada, Hinglish, and Kanglish** fluently.
---
💻Prewview or Demo (1)
<img width="1362" height="654" alt="image" src="https://github.com/user-attachments/assets/e1423e3e-2b2e-492a-b338-15217eadd2d8" />
---

## ✨ Key Features

* **⚡ Lightning Fast:** Powered by **Groq API (Llama 3.1)**, generating responses in milliseconds.
* **💎 Luxury Web UI:** A premium "Glassmorphism" interface built with Flask, HTML5, and CSS3.
* **🗣️ True Polyglot:**
    * **English:** Instant robotic response (Offline engine).
    * **Kannada (ಕನ್ನಡ) & Hindi (हिंदी):** Native script support with high-quality Google TTS.
    * **Code-Switching:** Understands mixed languages like **"Hinglish"** and **"Kanglish"**.
* **🎤 Smart Listening:** Auto-calibrates to background noise to prevent "nonsense" inputs.
* **🧠 Context Aware:** Switch modes instantly between Pure Language and Mixed conversational styles.

---

## 🛠️ Tech Stack

* **Core:** Python 3.12
* **Web Framework:** Flask
* **AI Model:** Llama-3.1-8b-instant (via Groq API)
* **Speech-to-Text:** Google Speech Recognition
* **Text-to-Speech:** `pyttsx3` (Offline Fast) & `gTTS` (Online High-Quality)
* **Audio Engine:** Pygame & Pyaudio


---
💻Prewview or Demo (2)
<img width="1365" height="645" alt="image" src="https://github.com/user-attachments/assets/c38acebf-3561-4a9d-8d5e-c25022822c80" />

---
## 🚀 Getting Started

Follow these steps to set up the Genius AI on your local machine.

### Prerequisites
* Python 3.8 or higher installed.
* A microphone connected to your PC.
* A free API Key from [Groq Cloud](https://console.groq.com/).

### 1. Clone the Repository
```bash
git clone [https://github.com/yourusername/genius-ai.git](https://github.com/yourusername/genius-ai.git)
cd genius-ai
2. Install Dependencies
Bash

pip install -r requirements.txt
(Note: If pyaudio fails on Windows, run pip install pipwin && pipwin install pyaudio)

3. Configure API Key
Open main.py and paste your Groq API Key in the settings section:

Python

# main.py
GROQ_API_KEY = "gsk_..."  # <--- Paste your key here
🖥️ Usage
Run the application with a single command. This will start the backend server and automatically launch the Luxury UI in your default browser.

Bash

python main.py
Modes Available:
English: Standard, fast responses.

Kanglish: Mix of Kannada grammar + English words (e.g., "Oota aita?").

Pure Kannada: Speaks and reads native Kannada script (e.g., "ಊಟ ಆಯ್ತಾ?").

Pure Hindi: Speaks and reads native Hindi script (e.g., "नमस्ते").

Hinglish: Mix of Hindi grammar + English words.

📂 Project Structure
Plaintext

genius-ai/
│
├── main.py            # The Brain (Flask Server + Audio Logic)
├── prompts.py         # AI Personality & System Instructions
├── requirements.txt   # Dependency List
└── templates/         # The Look (UI)
    └── index.html     # Luxury Glassmorphism Interface
⚠️ Troubleshooting
1. TemplateNotFound: index.html

Ensure you have a folder named templates and index.html is inside it.

2. Microphone not listening / "Silence Detected"

Check your Windows Sound settings.

Speak louder during the calibration phase (first 1 second).

3. 404 Error / API Error

Check your internet connection.

Verify your Groq API Key is correct in main.py.

🤝 Contributing
Contributions are welcome! If you have ideas for a "Dark Mode" or new languages:

Fork the project.

Create your feature branch (git checkout -b feature/AmazingFeature).

Commit your changes.

Push to the branch.

Open a Pull Request.

📜 License
Distributed under the MIT License. See LICENSE for more information.

<p align="center"> Built with ❤️ for the AI Community. </p>

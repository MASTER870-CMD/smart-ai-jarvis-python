
import os
import time
import re
import threading
import webbrowser
import speech_recognition as sr
from openai import OpenAI
import pyttsx3
from gtts import gTTS
import pygame
from flask import Flask, render_template, jsonify
import logging

# IMPORT YOUR PROMPTS
import prompts  

# ==========================================
#        USER SETTINGS
# ==========================================
GROQ_API_KEY = ""
ROBOT_SPEED = 175 

# ==========================================
#        FLASK SERVER & SHARED STATE
# ==========================================
# We mute the flask logs so they don't clutter the terminal
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

# This dictionary shares data between the Website and the Python Logic
shared_data = {
    "status": "idle",       # idle, listening, processing, speaking, stopped
    "last_text": "",        # The last thing said
    "mode": None,           # The selected language mode
    "running": True         # Control flag
}

# ==========================================
#        AI & VOICE SETUP
# ==========================================
engine = pyttsx3.init()
engine.setProperty('rate', ROBOT_SPEED)
voices = engine.getProperty('voices')
if len(voices) > 1: engine.setProperty('voice', voices[1].id)

client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=GROQ_API_KEY)

def play_audio(filename):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.quit()
    except: pass

def speak(text, force_google_lang=None):
    shared_data["status"] = "speaking"
    shared_data["last_text"] = text
    text_clean = text.replace("*", "")

    # Logic: Choose Voice
    use_google = False
    lang_code = 'en'
    if force_google_lang:
        use_google = True; lang_code = force_google_lang
    elif re.search(r'[\u0900-\u097F\u0C80-\u0CFF]', text_clean):
        use_google = True
        lang_code = 'kn' if re.search(r'[\u0C80-\u0CFF]', text_clean) else 'hi'

    if use_google:
        try:
            tts = gTTS(text=text_clean, lang=lang_code, slow=False)
            fname = f"temp_{int(time.time())}.mp3"
            tts.save(fname)
            play_audio(fname)
            os.remove(fname)
        except: pass
    else:
        try:
            engine.say(text_clean)
            engine.runAndWait()
        except: pass
    
    shared_data["status"] = "listening"

def get_response(text, prompt):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "system", "content": prompt}, {"role": "user", "content": text}],
            temperature=0.7, max_tokens=40
        )
        return completion.choices[0].message.content
    except: return "Connection error."

# ==========================================
#        BACKGROUND VOICE THREAD
# ==========================================
def assistant_logic():
    recognizer = sr.Recognizer()
    
    # Wait until user selects a mode on the website
    while shared_data["mode"] is None:
        if not shared_data["running"]: return
        time.sleep(0.5)

    # Configure Mode
    choice = shared_data["mode"]
    active_prompt = prompts.get_prompt(choice)
    
    listen_lang = "en-IN"
    forced_voice = None
    if choice == '3': listen_lang = "kn-IN"; forced_voice = "kn"
    elif choice == '4': listen_lang = "hi-IN"; forced_voice = "hi"

    speak("System Online.", forced_voice)
    shared_data["status"] = "listening"

    # Main Loop
    while shared_data["running"]:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
                
                shared_data["status"] = "processing"
                text = recognizer.recognize_google(audio, language=listen_lang)
                shared_data["last_text"] = text
                
                if "stop" in text.lower() or "exit" in text.lower():
                    speak("Goodbye.", forced_voice)
                    os._exit(0)

                response = get_response(text, active_prompt)
                speak(response, forced_voice)

        except:
            shared_data["status"] = "listening" # Reset if silence

# ==========================================
#        WEB ROUTES (THE BRIDGE)
# ==========================================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    return jsonify(shared_data)

@app.route('/start_mode/<mode>')
def start_mode(mode):
    shared_data["mode"] = mode
    return "OK"

@app.route('/shutdown')
def shutdown():
    shared_data["running"] = False
    shared_data["status"] = "stopped"
    
    # Give it a second to say goodbye then kill process
    def kill():
        time.sleep(1)
        os._exit(0)
    threading.Thread(target=kill).start()
    return "Bye"

# ==========================================
#        MAIN STARTUP
# ==========================================
if __name__ == "__main__":
    if "PASTE" in GROQ_API_KEY:
        print("❌ ERROR: Paste Key in main.py!")
    else:
        # 1. Start Voice Assistant in Background
        thread = threading.Thread(target=assistant_logic)
        thread.daemon = True
        thread.start()

        # 2. Open Browser Automatically
        webbrowser.open('http://127.0.0.1:5000')

        # 3. Start Web Server
        app.run(port=5000)
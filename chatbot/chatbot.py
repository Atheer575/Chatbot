import cohere
import whisper
import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
import tkinter as tk
from tkinter import messagebox

# Load Whisper
whisper_model = whisper.load_model("base")

# Initialize
engine = pyttsx3.init()

# Cohere
co = cohere.Client("P9JnoMA4GKnyuCnE21VIF1MnBnov5OKZoaWJY9zM") 

def record_audio(filename="input.wav", duration=5):
    fs = 44100
    try:
        sd.default.device = None 
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        write(filename, fs, recording)
        return filename
    except Exception as e:
        messagebox.showerror("Error", f"Recording failed: {e}")
        return None

def transcribe_audio(filename="input.wav"):
    result = whisper_model.transcribe(filename, task="translate", language="Arabic")
    return result["text"]

def get_bot_reply(text):
    response = co.generate(
        model='command',
        prompt=text,
        max_tokens=100
    )
    return response.generations[0].text.strip()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def run_chat():
    status_label.config(text="🎙️ Recording...")
    root.update()

    audio_file = record_audio()
    if not audio_file:
        return

    status_label.config(text="📝 Transcribing...")
    root.update()
    user_text = transcribe_audio(audio_file)
    user_label.config(text="You: " + user_text)

    if "exit" in user_text.lower():
        root.quit()

    status_label.config(text="🤖 Generating reply...")
    root.update()
    bot_reply = get_bot_reply(user_text)
    bot_label.config(text="Bot: " + bot_reply)

    speak(bot_reply)
    status_label.config(text="✅ Done")

# ---------------- GUI with tk ----------------
root = tk.Tk()
root.title("Voice Chatbot")
root.geometry("420x350")

title = tk.Label(root, text="🎧 Real-Time Voice Chatbot", font=("Arial", 16))
title.pack(pady=10)

record_btn = tk.Button(root, text="🎤 Start Talking", font=("Arial", 12), command=run_chat)
record_btn.pack(pady=10)

user_label = tk.Label(root, text="You: ", font=("Arial", 12), wraplength=380, justify="right")
user_label.pack(pady=10)

bot_label = tk.Label(root, text="Bot: ", font=("Arial", 12), wraplength=380, justify="right")
bot_label.pack(pady=10)

status_label = tk.Label(root, text="Idle", font=("Arial", 10), fg="gray")
status_label.pack(pady=10)

root.mainloop()
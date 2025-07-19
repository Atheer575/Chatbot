# Real-Time Voice Chatbot

## Introduction
This project is a simple voice-based chatbot. I speak into the microphone, the program understands what I said, sends it to an AI model, and then speaks back the answer. Everything happens live, with a basic user interface that works in both Arabic and English.

---

## What I Used
- Whisper by OpenAI — to convert my voice into text
- Cohere API — to generate a smart response based on my input
- pyttsx3 — to read the response out loud
- Tkinter — to create a very simple interface
- FFmpeg — needed for audio processing
- Python — the programming language used to build everything

---

# Code Snippet + Explanation
Record voice from microphone and save it

```python
def record_audio(filename="input.wav", duration=5):
fs = 44100
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
write(filename, fs, recording)
```

Transcribe Arabic speech and translate it to English

```python
def transcribe_audio(filename="input.wav"):
result = whisper_model.transcribe(filename, task="translate", language="Arabic")
return result["text"]
```

Send text to Cohere API and get a reply

```python
def get_bot_reply(text):
response = co.generate(
model='command',
prompt=text,
max_tokens=100
)
return response.generations[0].text.strip()
```

Speak the reply using text-to-speech

```python
def speak(text):
engine.say(text)
engine.runAndWait()
```

This part of the code handles recording, converting the speech to English, sending it to the AI model, and speaking the answer back.

---

## Output
Below are two examples showing how the chatbot responded:

### Example 1:
I said: "Hello, my name is Atheer"
Bot replied: "Nice to meet you Atheer. How can I assist you today?"

### Example 2:
I said: "Talk to me more about the AI model that you have"
Bot replied: "Sure! I am powered by Cohere, which is an advanced language model trained to understand and generate human-like text."

---

## What I Learned
- How to build a basic voice-controlled chatbot from scratch
- How to use Whisper to translate Arabic voice to English text
- How to connect and send messages to a real AI model (Cohere)
- How to make the program speak back using text-to-speech
- How to build a GUI using Tkinter
- How to organize everything and upload it to GitHub


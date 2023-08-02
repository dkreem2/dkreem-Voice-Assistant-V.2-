import openai
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import Scrollbar, Text, INSERT, END

# Step 3: Set up OpenAI GPT-3.5 API
openai.api_key = "OpenAI GPT-3.5 API"

# Step 4: Define the AI Voice Assistant Function
class VoiceAssistant(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Voice Assistant")
        self.geometry("1920x1080")

        self.init_voice_engine()
        self.init_gui()

    def init_voice_engine(self):
        self.engine = pyttsx3.init()

        # Configure voice options
        voices = self.engine.getProperty('voices')
        # Assuming "voices[0]" is a male voice, "voices[1]" is a female voice
        self.engine.setProperty('voice', voices[0].id)

    def init_gui(self):
        self.text_box = Text(self, wrap='word', font=("Arial", 12))
        self.text_box.pack(expand=True, fill='both')
        self.text_box.configure(state='disabled')

        scrollbar = Scrollbar(self, command=self.text_box.yview)
        scrollbar.pack(side='right', fill='y')
        self.text_box['yscrollcommand'] = scrollbar.set

        self.listen_button = tk.Button(self, text="Listen", command=self.listen_for_user_input)
        self.listen_button.pack()

    def listen_for_user_input(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            self.display_message("Listening...")
            audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio).lower()
            self.display_message("You: " + user_input)

            # TODO: Implement intent recognition to extract intent from the query

            # Translate user input to English (if needed) for GPT-3.5 API
            # TODO: Implement language detection and translation if necessary

            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=user_input,
                max_tokens=150,
                temperature=0.7,
            )

            ai_response = response.choices[0].text.strip()
            self.display_message("AI: " + ai_response)

            self.speak(ai_response)

        except sr.UnknownValueError:
            self.display_message("AI: Sorry, I didn't catch that. Could you please repeat?")
            self.speak("Sorry, I didn't catch that. Could you please repeat?")

        except sr.RequestError as e:
            self.display_message(f"AI: Oops! There was an error with the speech recognition service. {e}")
            self.speak("Oops! There was an error with the speech recognition service.")

    def speak(self, text):
        self.display_message("AI is speaking...")
        self.engine.say(text)
        self.engine.runAndWait()
        self.display_message("AI finished speaking.")

    def display_message(self, message):
        self.text_box.configure(state='normal')
        self.text_box.insert(INSERT, message + "\n")
        self.text_box.configure(state='disabled')
        self.text_box.see(END)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    voice_assistant = VoiceAssistant()
    voice_assistant.run()

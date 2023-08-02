# Voice Assistant

Voice Assistant is a simple Python-based voice-controlled assistant that utilizes the OpenAI GPT-3.5 API for natural language processing and understanding. This project allows users to interact with the assistant through speech input, and it responds by generating appropriate text-based responses and even speaks them out using text-to-speech technology.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Key](#api-key)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Voice Assistant is a simple AI-powered voice assistant that can understand natural language commands and provide meaningful responses. It uses the OpenAI GPT-3.5 API to generate responses based on the user's input. The assistant is equipped with a text-to-speech engine that allows it to speak its responses to the user.

The graphical user interface (GUI) is built using the Tkinter library, providing a convenient way to interact with the assistant. When the "Listen" button is pressed, the assistant starts listening to the user's voice input via the microphone. After processing the user's query and generating a response from the GPT-3.5 API, the assistant displays the conversation history in the text box and also speaks the response.

## Features

- Voice-based interaction with the AI assistant.
- Natural language processing and understanding using the OpenAI GPT-3.5 API.
- Text-to-speech capability for the AI's responses.
- Simple and intuitive graphical user interface (GUI) built with Tkinter.

## Requirements

To run the Voice Assistant, you'll need the following dependencies:

- Python 3.x
- openai
- speech_recognition
- pyttsx3
- tkinter

You can install the required libraries using pip:

```
pip install openai
```
```
pip install speechrecognition
```
```
pip install pyttsx3
```

## Installation

To use the Voice Assistant, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/voice-assistant.git
```
```
cd voice-assistant
```

2. Install the required dependencies as mentioned in the [Requirements](#requirements) section.

## Usage

1. Run the `voice_assistant.py` script:

```
python dkreem_v2.py
```

2. The Voice Assistant application window will appear.

3. Click on the "Listen" button and start speaking to the assistant.

4. The assistant will process your speech, display the conversation history, and respond both visually and audibly.

## API Key

For the Voice Assistant to interact with the OpenAI GPT-3.5 API, you need to provide your own API key. Replace the placeholder API key in the `voice_assistant.py` file with your actual OpenAI API key.

```
openai.api_key = "your_openai_api_key_here"
```

If you don't have an OpenAI API key, you can sign up for access at [OpenAI's website](https://openai.com).

## Contributing

Contributions are welcome! If you have any improvements or additional features to propose, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

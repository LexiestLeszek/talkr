# Talkr: A Conversational Assistant

Talkr is a Python-based conversational assistant that listens for spoken commands, processes them, and provides a spoken response. It utilizes speech recognition and text-to-speech technologies to interact with users in a natural, conversational manner.

## Features

- **Speech Recognition**: Talkr uses the `speech_recognition` library to transcribe spoken commands into text.
- **Text-to-Speech**: The `pyttsx3` library is employed to convert text responses into spoken words.
- **Natural Language Processing**: The `whisper` library is used for speech-to-text transcription, and `ollama` for generating human-like responses.

## Getting Started

To get started with Talkr, you'll need to have Python installed on your system. Follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/LexiestLeszek/talkr.git
   ```
2. Navigate to the project directory:
   ```
   cd talkr
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
4. Run the main script:
   ```
   python talkr.py
   ```

## Usage

Once the script is running, Talkr will listen for commands and respond accordingly. You can interact with it by speaking commands and it will provide responses.

## Contributing

Contributions to Talkr are welcome! If you have a feature request, bug report, or want to contribute code, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

If you have any questions or suggestions, please open an issue.

## Acknowledgements

- The `speech_recognition` library for enabling speech recognition.
- The `pyttsx3` library for text-to-speech capabilities.
- The `whisper` and `ollama` libraries for natural language processing and response generation.

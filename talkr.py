import os
import whisper
import sys
import ollama
import speech_recognition as sr
mic = sr.Microphone()
recognizer = sr.Recognizer()

def speech2text():
    '''
    Function to transcribe an audio file to text using OpenAI Speech API or locally 
    '''
    with mic as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(mic)
        audio = recognizer.listen(mic)
    
    with open("command.wav", "wb") as f:
        f.write(audio.get_wav_data())
    
    text = whisper.load_model("base").transcribe("command.wav")["text"]
    
    return text

def ask_llm(prompt):
    """ 
    Function to answer question by autocompletion 
    """
    response = ollama.chat(model='qwen:0.5b', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    answer = response['message']['content']
    return answer

def main():
    
    while True:
    
        command = speech2text()
        if command is not None:
            print(f"Human: {command}")
            answer = ask_llm(command)
            print(f"Chatbot: {answer}")
            command = None

if __name__ == '__main__':
  main()

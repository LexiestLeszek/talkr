import whisper
import ollama
import speech_recognition as sr
import pyttsx3

source = sr.Microphone()
recognizer = sr.Recognizer()
engine = pyttsx3.init() # talking engine
engine.setProperty('rate', 180) # setting the speed of talking
wh = whisper.load_model("tiny")

def listen():

    with source as s:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
        with open("command.wav", "wb") as f:
            f.write(audio.get_wav_data())
        
        text = wh.transcribe("command.wav")["text"]
        
        return text

def respond(text):
    engine.say(text)
    engine.runAndWait() 

def ask_llm(prompt):
    
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
    
        command = listen()
        if command is not None:
            print(f"Human: {command}")
            answer = ask_llm(command)
            print(f"Bot: {answer}")
            respond(answer)
            command = None

if __name__ == '__main__':
  main()

import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)  # Use the variable text instead of the string "text"
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Obtain audio from the microphone
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            command = recognizer.recognize_google(audio)
            print("You said: " + command)

            # Check for the wake word "Jarvis"
            if "jarvis" in command.lower():
                # Process commands after the wake word
                print("How can I assist you?")
                # Here you can add more commands to process

            if "thanks" in command.lower():
                # Process commands after the wake word
                print("Always here for you sir.")
                speak("Always here for you sir.")
                break
                
                # Here you can add more commands to process
            else:
                print("Wake word not detected.")

        except sr.UnknownValueError:
            print("Google could not understand audio")
        except sr.RequestError as e:
            print("Google error; {0}".format(e))
            
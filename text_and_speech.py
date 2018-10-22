import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os


class TextAndSpeech(object):
    def __init__(self):
        print("Initialize text and speech module")

    def speech_input(self):
        r = sr.Recognizer()

        asking_line = "What can I do for you?"
        print(asking_line)
        self.text_to_speech(asking_line)

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            os.system("clear")
            print(asking_line)
            print("I am listening")
            audio = r.listen(source)

        return r, audio

    def speech_to_text(self, r, audio):
        try:
            command_text = r.recognize_google(audio, language="en-US")  # may need to add default API key later, key="AIzaSyBKXvt_wq_YtiOERo0WGPhFXvmuZpiRRMw"
            print("Command inputted " + command_text)
            return command_text
        except sr.UnknownValueError:
            print("Unknown Value Error")
            return "Error"
            self.text_to_speech("Unknown Value Error.")
        except sr.RequestError:
            print("Request Error")
            return "Error"
            self.text_to_speech("Request Error.")

    def text_to_speech(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save("temp.mp3")
        output_speech = AudioSegment.from_mp3("temp.mp3")
        play(output_speech)
        os.remove("temp.mp3")

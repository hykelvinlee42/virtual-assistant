"""
$$\   $$\ $$\     $$\       $$\   $$\          $$\            $$\                 $$\
$$ |  $$ |\$$\   $$  |      $$ | $$  |         $$ |           \__|                $$ |
$$ |  $$ | \$$\ $$  /       $$ |$$  / $$$$$$\  $$ |$$\    $$\ $$\ $$$$$$$\        $$ |      $$$$$$\   $$$$$$\
$$$$$$$$ |  \$$$$  /        $$$$$  / $$  __$$\ $$ |\$$\  $$  |$$ |$$  __$$\       $$ |     $$  __$$\ $$  __$$\
$$  __$$ |   \$$  /         $$  $$<  $$$$$$$$ |$$ | \$$\$$  / $$ |$$ |  $$ |      $$ |     $$$$$$$$ |$$$$$$$$ |
$$ |  $$ |    $$ |          $$ |\$$\ $$   ____|$$ |  \$$$  /  $$ |$$ |  $$ |      $$ |     $$   ____|$$   ____|
$$ |  $$ |    $$ |$$\       $$ | \$$\\$$$$$$$\ $$ |   \$  /   $$ |$$ |  $$ |      $$$$$$$$\\$$$$$$$\ \$$$$$$$\
\__|  \__|    \__|\__|      \__|  \__|\_______|\__|    \_/    \__|\__|  \__|      \________|\_______| \_______|
"""
from text_and_speech import TextAndSpeech
from operations import Operations
from interface import Interface
from time import sleep
from os import system
import threading
import gi
gi.require_version("Gtk", "3.0")

music_folder_dir = "/home/k0042n/Music/"  # directory of your music folder: /home/name/Music/
openweathermap_api = "422c0a86a953386e6373a43b45dfbb7a"  # openweathermap.org API token
fixer_api = "eb95fbc5122999debe2a0dcd7bd4372c"  # fixer.io API token
newsapi_api = "de49bc8d15d24c4a835f34457ae54d2a"  # newsapi_org API token


class Bot(object):
    def __init__(self):
        self.ts = TextAndSpeech()
        self.operations = Operations()
        self.windows = Interface()
        sleep(1)
        system("clear")

    def decide_action(self):
        r, audio = self.ts.speech_input()
        command = self.ts.speech_to_text(r, audio)

        if command == "fun":
            self.action_joke()
            return False
        elif command == "music":
            self.action_music()
            return False
        elif command == "weather":
            self.action_weather()
            return False
        elif command == "currency":
            self.action_currency()
            return False
        elif command == "news":
            self.action_news()
            return False
        elif command == "stop":
            return True
        else:
            error_message = "I don't understand. "
            # Debug purpose
            print(error_message + command)
            self.ts.text_to_speech(error_message)
            return False

    def action_joke(self):
        joking = self.operations.joke()
        self.ts.text_to_speech(joking)
        sleep(2)

    def action_music(self):
        self.ts.text_to_speech("Playing music")
        self.windows.update_label("It's music time!")
        self.operations.music(music_folder_dir)

    def action_weather(self):
        weather_report = self.operations.weather(openweathermap_api)
        self.ts.text_to_speech(weather_report)
        sleep(2)

    def action_currency(self):
        currency_report = self.operations.currency(fixer_api)
        self.ts.text_to_speech(currency_report)
        sleep(2)

    def action_news(self):
        news_report_title, news_report_description = self.operations.news(newsapi_api)
        self.windows.update_label(news_report_title)
        self.ts.text_to_speech(news_report_title)
        self.windows.update_label(news_report_description)
        self.ts.text_to_speech(news_report_description)
        sleep(2)

    def main(self):
        while True:
            flag = self.decide_action()
            if flag:
                break

    def call_window(self):
        self.windows.show_all()
        self.windows.run()


if __name__ == "__main__":
    bot = Bot()
    bot_thread = threading.Thread(target=bot.main)
    bot_thread.daemon = True
    bot_thread.start()
    bot.call_window()

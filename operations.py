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
import random
import os
from pydub import AudioSegment
from pydub.playback import play
import requests
import json


class Operations(object):
    def __init__(self):
        print("initialize operations module")

    def joke(self):
        jokes = [
            "I never make mistakes. I thought I did once, but I was wrong.",
            "I can totally keep secrets. It's the people I tell them to that can't.",
            "What do you call a cow with two legs? Lean beef.",
            "What is the difference between a snowman and a snowwoman? Snowballs."
        ]
        response = random.choice(jokes)

        print(response)
        return response

    def music(self, music_dir):
        music = os.listdir(music_dir)
        music_selection = music_dir + random.choice(music)

        song = AudioSegment.from_mp3(music_selection)
        play(song)

    def get_locationAndIP(self):
        request = requests.get("http://ip-api.com/json")
        json_data = json.loads(request.text)
        lat = json_data['lat']
        lon = json_data['lon']
        ip = json_data['query']

        return lat, lon, ip

    def weather(self, api):
        lat, lon, ip = self.get_locationAndIP()

        request_url = "http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s" % (lat, lon, api)
        request = requests.get(request_url)
        json_data = json.loads(request.text)

        temperature = json_data['main']['temp'] - 273.15
        description = json_data['weather'][0]['description']
        area = json_data['name']
        response = "The temperature is now " + str(temperature) + " degree Celsius and " + description + " in " + area

        print(response)
        return response

    def currency(self, api):
        request_url = "http://data.fixer.io/api/latest?access_key=" + api  # base currency for free fixer.io api is EUR
        request = requests.get(request_url)
        json_data = json.loads(request.text)

        base_currency = "European dollar"
        convert_currency = "US dollars"  # default conversion: EUR to USD
        conversion_rate = json_data['rates']['USD']

        response = "One dollar of " + base_currency + " is now " + str(conversion_rate) + " " + convert_currency
        print(response)
        return response

    def news(self, api):
        area = "us"  # default area: US

        request_url = "https://newsapi.org/v2/top-headlines?country=" + area + "&apiKey=" + api
        request = requests.get(request_url)
        json_data = json.loads(request.text)

        total_result = json_data['totalResults']
        result = random.randint(0, total_result)

        response_title = json_data['articles'][result]['title']
        response_description = json_data['articles'][result]['description']
        return response_title, response_description

#!/usr/bin/python3
# General Public License (GPL) v3.0 .

import sys
import requests
import json

class WeatherShell:
    def __init__(self):
        
        # figlet used for ASCII

        icon = open('icon.txt', 'r')
        
        icon_contents = icon.read()

        print(icon_contents)

        icon.close()

        city = ""
        
        if len(sys.argv) < 2:
            print("ERROR: Syntax : python3 WeatherShell.py CITY_NAME")
            return
        else:
            city = " ".join(sys.argv[1:])
        
        # API: https://weatherstack.com

        API_TOKEN = "40eb6171b44c2913a50342a5bb265fd3"

        API_URL = "http://api.weatherstack.com/current?access_key=" + API_TOKEN + "&query=" + city

        response = requests.get(API_URL).text
        data = json.loads(response)

        if "error" in data.keys():
            print("ERROR: Connection failed")
            return

        current = data["current"]

        print("--------------------NOW--------------------")

        print("\nIt's " + str(current["temperature"]) + " C now. " + current["weather_descriptions"][0])
            
        print("\n ----- Updated at " + str(current["observation_time"]) + " GMT ----- ")

        print("\nMore info? [Y/N]")

        answer = input()

        if answer == 'Y' or answer == 'y':
            self.moreInfo(current)

    def moreInfo(self, current):
        for key in current:
            print(str(key) + " : " + str(current[key]))


def main():
    WeatherShell()

if __name__ == "__main__":
    main()

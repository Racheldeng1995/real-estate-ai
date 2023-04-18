import os
import requests
import json

class ZillowAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://zillow56.p.rapidapi.com/search"

    def get_search_results(self, city, state):
        headers = {
           "X-RapidAPI-Key": self.api_key,
	       "X-RapidAPI-Host": "zillow56.p.rapidapi.com"
        }
        print(headers)
        params = {
            "location": city + ', ' + state
        }
        print(params)
        response = requests.request("GET", self.endpoint, headers=headers, params=params)
        print(response.status_code)

        if response.status_code == 404:
            print(f"404 Error: {response.reason}")

        if response.status_code == 200:
            data = json.loads(response.text)
            print(data)
            return data['results']
        else:
            return None

import os
import requests
from flask import Flask, render_template, request
from zillow.zillow import ZillowAPI

app = Flask(__name__)

# Read API key from file
with open('zillow/api_key.txt', 'r') as file:
    api_key = file.read().replace('\n', '')
    print(api_key)

# Initialize ZillowAPI object
zillow_api = ZillowAPI(api_key)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Search results page
@app.route('/search')
def search():
    city = request.args.get('city')
    state = request.args.get('state')
    data = zillow_api.get_search_results(city, state)
    print(data)
    return render_template('search_results.html', search_query=f'{city}, {state}', search_results=data)

if __name__ == '__main__':
    app.run(debug=True)

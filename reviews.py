import os
import requests




API_KEY = os.getenv('MY_API_KEY')
PLACE_ID = os.getenv('MY_PLACE_ID')

url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={PLACE_ID}&key={API_KEY}&fields=reviews'

response = requests.get(url)
data = response.json()

reviews = data['result']['reviews']

for review in reviews:
    print(f"Author: {review['author_name']}")
    print(f"Rating: {review['rating']}")
    print(f"Text: {review['text']}")
    print('----')

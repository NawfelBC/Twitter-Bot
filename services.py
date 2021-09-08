import json
import random
from typing import Dict, List
import requests

def download_image(image_url):
    filename = 'picture.jpg'
    image_response = requests.get(image_url, stream=True)
    if image_response.status_code == 200:
        with open(filename, 'wb') as image_file:
            for chunk in image_response:
                image_file.write(chunk)

def get_movies() -> List:

    with open('data.json', encoding='utf-8') as movies_file:
        movies = json.load(movies_file)

    return movies

def get_random_movie() -> Dict:

    movies = get_movies()
    movie = random.choice(movies)

    return movie

def tweet_formater(movie: Dict[str, str]) -> str:

    title = movie['title']
    release_date = movie['release_date']
    rate = movie['rate']
    image = movie['image']
    if rate == 'N/A':
        tweet = f'{title} ({release_date})'
    else:
        tweet = f'{title} ({release_date}) ⭐{rate}'

    return tweet,image

def get_tweet():
    while True:
        movie = get_random_movie()
        tweet,image = tweet_formater(movie)
        return tweet,image
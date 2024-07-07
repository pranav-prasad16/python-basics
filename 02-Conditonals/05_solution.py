import random

weather = {'Sunny': 'Go for a Walk', 'Rainy': 'Read a book', 'Snowy': 'Build a snowman'}

random_weather = random.choice(list(weather.keys()))

print(f'{random_weather}: {weather[random_weather]}')
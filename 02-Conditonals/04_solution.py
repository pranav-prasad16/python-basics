import random

fruit = "Banana"
color = ['green', 'yellow', 'brown']

random_color = random.choice(color)

if fruit == "Banana":
    if random_color == 'green':
        print('The banana is Unripe')
    elif random_color == 'yellow':
        print('The banana is Ripe')
    else:
        print('The banana is Overripe')
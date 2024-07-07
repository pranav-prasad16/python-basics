import random

age = int(input('Enter you age : '))

day = random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

ticket_price = 0

if age < 18 :
    ticket_price = 8

else :
    ticket_price = 12

print(day)

if day == 'Wednesday':
    ticket_price -= 2
    print(f'Your ticket price because of wednesday discount is : {ticket_price}')

print(f'Your ticket price is : {ticket_price}')
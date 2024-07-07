password = '123n@'

if len(password) < 6:
    print('Weak password')
elif len(password) < 8:
    print('Decent password')
else:
    print('Strong password')
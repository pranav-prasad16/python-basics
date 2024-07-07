coffee_order = 'Medium'
extra_shot = 'False'

if coffee_order == 'Small':
    if extra_shot == True:
        print('Small coffee with extra shot of espresso')
    else:
        print('Small coffee')
elif coffee_order == 'Medium':
    if extra_shot == True:
        print('Medium coffee with extra shot of espresso')
    else:
        print('Medium coffee')
else:
    if extra_shot == True:
        print('Large coffee with extra shot of espresso')
    else:
        print('Large coffee')

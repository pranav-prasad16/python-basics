year = 2024

if year%400 == 0:
     print('The year is leap year')

if year%4 == 0:
        if year%100 != 0:
            print('The year is leap year')
else:
    print('The year is not leap year')
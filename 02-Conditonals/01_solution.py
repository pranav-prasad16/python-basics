age = input('Enter your age : ')
age_in_int = int(age)

if age_in_int < 13 :
    print('Child')

elif 13 <= age_in_int <= 19 : 
    print('Teenager')

elif 20 <= age_in_int < 60 :
    print('Adult')

else :
    print('Senior')
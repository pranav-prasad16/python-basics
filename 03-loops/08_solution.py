num = 5
flag = True
for i in range(2, num):
    if num%i == 0:
        flag = False
        break
if flag == False:
    print('The num is Co-prime')
else:
    print('The num is prime')
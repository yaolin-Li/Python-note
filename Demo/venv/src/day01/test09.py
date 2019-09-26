import random

answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input('Please input number:'))
    if number < answer:
        print('bigger')
    elif number > answer:
        print('smaller')
    else:
        print("right!")
        break
print('You guess %d time'%counter)
if counter > 7:
    print('Please try your best')
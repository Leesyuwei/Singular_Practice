import random
#A=random.choice(range(7))
#print(A)

#A=random.choices(range(7),k=2)
#print(A)

#A=random.randint(1,6)
#print(A)

#A=random.normalvariate(0,1)
#print(A)

from microbit import *
while 1:
    if accelerometer.current_gesture() == 'shake':
        A=random.choice(range(1,7))
        display.show(A)
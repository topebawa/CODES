from time import clock
start=clock()
value=eval(input('three multiplied by four: '))
if(value==12):
    print(clock()-start)


from time import clock
from random import random,randrange
time1=clock()
start=0
while (start<20):
        start+= 2
        print(start)
print(clock()-time1)


from time import sleep
for number in range(0,20,2):
    print(number)
    sleep(0.1)


print(randrange(5,10))

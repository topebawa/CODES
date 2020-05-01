import timeit
import random
######x = range(1,11,1)
######for n in x:
######    ##pop(0)
######    print(n)
######count_list
####
####numbers = range(1,11,1)
####count_list = []
####
####for n in numbers:
####    if n%2==0:
####        count_list.append(n**2)
####
####
####print(count_list)
##
##
i = range(1,11,1)
count_list = []
for n in i:
    count_list.append(n)
print(count_list)


'------------------------------------------------------'
i = range(1,11,1)
count_list = []
for n in i:
    if(n%2==0):
        count_list.append(n)

print(count_list)

'---------------------------------------------------------'


count_list = []
loop = 0
while loop < 10:
    i = random.randrange(1,10)
    count_list.append(i)
    loop += 1
print(count_list)

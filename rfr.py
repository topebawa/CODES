x=eval(input('enter a number here: '))
list=[]
for num in range(x,-1,-1):
    list+=[num]
print(list)




print('---------------------------------------------------')
def countdown(x):
    return[num for num in range(x,-1,-1)]
    
print(countdown(eval(input('enter a number here: '))))


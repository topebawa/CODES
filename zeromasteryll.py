##Conditional LOgic_____________________________
is_old = False
is_licensed = False

##if is_old:
##    print("You are old enough to drive!")
##elif is_licensed:
##    print("You can drive now!")
##else:
##    print("You are not old enough to drive")


if is_old and is_licensed:
    print("You are old enough and you have a license!")
else:
    if is_old:
        print("You are old enough but you do not have a license!")
    elif is_licensed:
        print("You are not old enough to drive, how did you get a license??")
    else:
        print("You are not old enough to have a license to drive this car")

##print(bool(0.56))

##Ternary Operators_________________________________
is_friend = False
can_message = "Message allowed" if is_friend else "not allowed to message"
print(can_message)

##For Loop___________________________________________
for item in {1,2,3,4,5,6}:
    for items in {'a','b','c'}:
        print(item,items)    

my_list = [1,2,3,4,5,6,7,8,9,10]
total = 0
for item in my_list:
    total = total+item
print(total)

##Range-------------------------------------------------
##for number in range(1):
##    print(tuple(range(0,10)))

##Enumerate________________________________________-
for i,char in enumerate(range(100)):
    print(i,char == 50)
for i,char in enumerate('hellooo'):
    print(i,char)

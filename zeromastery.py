##def highest_even(li):
##    evens = []
##    for item in li:
##        if item % 2 ==0:
##            evens.append(item)
##        return max(evens)
##
##print(highest_even([2,10,2,3,4,8,11]))
##
##
####print(type(2 + 4))
####print(type(2 - 4))
####print(2 * 4)
####print(type(2 / 4))
####print(type(20 + 1.1))
####
####print(type(1.1 + 0.9))
####print(3 // 2)
####print(10 % 7)
####
####range(100)
####list(range(100))
####
####
####def make_list(num):
####    result = []
####    for i in range(num):
####        result.append(i*2)
####    return result
####
####my_list = make_list(100)
####print(my_list)
##
##print(round(6.9))
##print(abs(-49))
##
##name = 'Tope'
##age = 22
##
##print('Your name is ' + name + ". You're " + str(age) + " Years old.")
##print(f"Your name is {name}. You're {age} years old")
##print("Your name is {}.  You're {} years old." .format(name,age))
##
##
##
##selfish = "me me me"
##print(selfish[0:7:2])
##
##
##
##birth_year = eval(input("What year were you born?: "))
##this_year = eval(input("What year is this?: "))
##age = this_year - birth_year
##
##print(f"You're {age} years old")
##
##
##
##user_name = input("Enter your username: ")
##password = input("Enter your password: ")
##a = "*" * len(password)
##
##print(f"{user_name} your password {a} is {len(password)} characters long")
##
##
##
##
##
##
##
##picture = [
##    [0,0,0,1,0,0,0],
##    [0,0,1,1,1,0,0],
##    [0,1,1,1,1,1,0],
##    [1,1,1,1,1,1,1],
##    [0,0,0,1,0,0,0],
##    [0,0,0,1,0,0,0]
##    ]
##
##for row in picture:
##    for pixel in row:
##        if (pixel == 1):
##            print("*", end = '')
##        else:
##            print(' ', end= '')
##    print('')
##
##
##
##
##
##print(list(range(1,100,2)))
##
##
##
##
##
##sentence = ' '
##new_sentence = sentence.join(['hi', 'my','name','is','jay'])
##print(new_sentence)
##
##
##
###LIST UNPACKING--------------------------
##
##a, *again,b,c = [1,2,3,4,5,6,7,8,9]
##print(a)
##print(again)
##print(b)
##print(c)
##
##
##
###dictionaries
##
##user = {
##    'name': [1,2,3],
##    'pass': 'game',
##    'cn': 'rue',
##    'cf': 'True',
##    'fb': 'True',
##    'gh': 'True',
##    'fg': 'True',
##    'er': 'True',
##    'h': 'True',
##    'g': 'True',
##    'f': 'True',
##    'e': 'True',
##    'd': 'True'
##    
##    }
####print(user.pop('name'))
##
##
##print(user)
##
##print(user.popitem())


my_list = [1,2,3,4,5,5]
print(set(my_list))


my_set = {1,2,3,4,5}
print(my_set)

my_list = [1,2,3,4,5]
print(my_list)

my_dictionary = {
    'a' : 'same',
    'b' : [1,2,3],
    'c' : 4,
    'age' : 55,
    '8' : 'yeah',
    6 : 'number'
    }
print(my_dictionary)
print(my_dictionary.items())




































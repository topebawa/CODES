import math
Question=input("What are you looking for? \nA)Hypotenuse \tB)Opposite \nC)Adjacent: ")
##if Question != "A,B,C":
    ##continue
   ## print("make sure the option you select is in uppercase")

if Question=="A":
    opposite=eval(input("Input your opposite value: "))
    adjacent=eval(input("Input your adjacent value: "))
    hypotenuse=(math.sqrt((opposite*opposite)+(adjacent*adjacent)))
    print('The hypotenuse is :', hypotenuse)
if Question=="B":
    hypotenuse=eval(input("Input your hypotenuse value: "))
    adjacent=eval(input("Input your adjacent value: "))
    opposite=(math.sqrt((hypotenuse*hypotenuse)-(adjacent*adjacent)))
    print('The opposite is :', opposite)
if Question=="C":
    hypotenuse=eval(input("Input your hypotenuse value: "))
    opposite=eval(input("Input your opposite value: "))
    adjacent=(math.sqrt((hypotenuse*hypotenuse)-(opposite*opposite)))
    print('The Adjacent is :', adjacent)

          
    


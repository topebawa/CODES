##NUMBER 1
#radius = eval(input("Enter your radius:"))
#pi = 3.142
#V = (4/3) * (radius**3)
#A = 4 * pi * (radius**2)
#print("\nThe volume and surface area of a sphere with radius", radius, "cm are", V, " cm and", A, "cm respectively")

##NUMBER 2
#print("Write a program that calculates the cost per square inch of a circular pizza")
#diameter = eval(input("Enter your diameter : "))
#radius = diameter / 2
#print("The value of your radius is", radius, "cm")
#pi = 3.142A = (pi * (radius**2))
#print("\nThe cost per square inch of a circular pizza of diameter", diameter,"cm and radius",radius,"cm is", A,"cm")

#number 3
#number 4

#NUMBER 6
##print("Calculate the slope of a line with coordinates (X1,Y1) and (X2,Y2)")
##x1 = eval(input("Enter coordinate X1: "))
##y1 = eval(input("Enter coordinate Y1: "))
##x2 = eval(input("Enter coordinate X2: "))
##y2 = eval(input("Enter coordinate Y2: "))
##
##
##slope = ((y2 - y1) / (x2 - x1))
##distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
##print("The slope for coordinates (", x1, ",",y1, ") and (", x2, ",", y2, ") is ", slope)
##print("The distance for coordinates (", x1, ",",y1, ") and (", x2, ",", y2, ") is ", distance)
##

##print("Write a program to calculate the molecular weight of C2H50H")
##C = 12.011
##H = 1.0079
##O = 15.994
##c = eval(input("Enter the number of moles for carbon: "))
##h = eval(input("Enter the number of moles for hydrogen: "))
##o = eval(input("Enter the number of moles for oxygen: "))
##
##s.i = ((C*c) + (H*h) + (O*o))
##print("The molecular weight of CH0H is", S.i);


##question 9:
##print("Calculate the area of a triangle")
##
##
##a = eval(input("Enter value of a :"))
##b = eval(input("Enter value of b :"))
##c = eval(input("Enter value of c :"))
##B = (a +  b + c) / 2
##
##A = (B*((B - a)*(B - b)*(B - c)))**0.5
##print("The area of the triangle is ", A)


##QUESTION 5:
##print("Calculate the cost of an order\n")
##n = no_of_cups = eval(input("Enter the number of cups you want to order: "))
##p = price_of_a_cup = 10.50
##s = shipping_fee_per_cup = 0.86
##f = fixed_cost = 1.50
##c = cost_of_an_order = ((p * n) + (s * n) + f)
##if n > 1:
##    print("The price for", n,"cups is $", c)
##else:

##    print("The price for", n,"cup is $", c)
##QUESTION 8 
year = eval(input("Enter a valid year here: "))

if 1000 <= year <= 99999:
      C = year / 100
      epact = (8 + (C//4) - C + ((8*C + 13//25) + 11 * (year%19)))%30
      print("The value of epact is", int(epact))
else:
        print("The year inputed has to be a 4 digit year")

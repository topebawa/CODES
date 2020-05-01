##x = 1
##last = 20
##c=3
##m=2
##
##for count in range(1,20):
##    x = eval(input("Enter your value: "))
##    y = (m*x) + c
##    for i,j in [(y,x)]:\
##        print(x,"in the equation will make y",y)
##
##print("Y\t X\t m\t c\n",y,"\t",x,"\t",m,"\t",c)
##print(i,j)
##

#! python3
from math import *

def bisection():
    a = 0
    b = 1
    mid = (a + b) / 2

    # finding f(a), f(b), f(mid) for the first iteration
    F_a = a * exp(a) - 1
    F_b = b * exp(b) - 1
    F_mid = mid * exp(mid) - 1

    # make sure initial test for while loop fails
    # by making sure the tolerance is > 0.05%
    prev_mid = mid * 2

    tolerance = abs((mid - prev_mid) / mid) * 100

    # loop until root is found or tolerance < 0.05%
    while round(tolerance, 2) > 0.05:
        # store value for previous iteration
        prev_mid = mid

        # change the boundaries of bisection depending on F_mid
        if (F_mid * F_a) > 0:
            a = mid
            F_a = F_mid
        elif (F_mid * F_a) < 0:
            b = mid
            F_b = F_mid
        else: # root has already been found
            break

        # recalculate middle of the range and F(mid) at the point
        mid = (a + b) / 2
        F_mid = mid * exp(mid) - 1

        tolerance = abs((mid - prev_mid) / mid) * 100

    return mid

if __name__ == '__main__':
    root = bisection()
    print("The root is:", root)

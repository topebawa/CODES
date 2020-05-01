from math import cos, pi, radians
##a = cos(radians(90))
##b = (pi * a) / 180
##print(b)
##print(pi)
def factorials (n):
    fact = 1
    for i in range (n,1,-1):
        fact = fact * i
        return fact
def main():
    print()
degree = eval(input("The angle in degree is: "))
n = int(input("The number of iterations is: "))
x = (pi * degree) / 180
sine = 0
for i in range (n):
    sum = (sum + (((-1) ** i) * x)**((2 * i) + 1)) / ((factorials)**((2 * i) + 1))
    sine = sine + sum
print(cos(x))
print (sum)
main()

#solving mathematical calculations
Response1=(eval(input('What do you want to solve for?:\n a)Area of Rectangle\t b)Area of Triangle\t c)Perimeter of Rectangle\n d) Celsius\t e)Area of Circle : \n')))
if (Response1=="a"):
    length=eval(input("enter the value of your length:"))
    breadth=eval(input("enter the value of your breadth:"))
    areaofrectangle=length*breadth
    print("the area of the rectangle with the length and breadth",length,"cm",breadth,"cm respectively is",areaofrectangle)

if (Response1=='b'):
    base=eval(input("enter the value of your base:"))
    height=eval(input("enter the value of your height:"))
    areaofTriangle= 0.5*(base*height)
    print("the area of the triangle with the base and height",base,"cm",height,"cm respectively is",areaofTriangle)

if (Response1=='c'):
    length=eval(input("enter the value of your length:"))
    breadth=eval(input("enter the value of your breadth:"))
    perimeterofrectangle= 2*(length+breadth)
    print("the perimeter of the rectangle with the length and breadth",length,"cm",breadth,"cm respectively is",perimeterofrectangle)
    
if (Response1=='d'):
    F= eval(input("enter the value of your farenheit:"))
    Celsius=(5/9)*(F-32)
    print(F,"farenheit is",Celsius)
    
if (Response1=='e'):
    radius=eval(input("enter the value of your radius:"))
    pi=3.14
    areaofCircle= pi*(radius**2)
    print("the area of the circle with radius",radius,"cm is",areaofCircle)







 






#solving mathematical areas

trials=0
trials+=1
question=3
while 1==1:
    Response1=(input('What do you want to find?: \na)Area of Rectangle \nb)Perimeter of Rectangle\nc)Area of Triangle \nd)Area of Circle \ne)Celsius \n===>\n'))
    if (Response1=='a'):
        length=eval(input("enter the value of your length:"))
        breadth=eval(input("enter the value of your breadth:"))
        area=length*breadth
        print("\nThe area of the rectangle with the length and breadth",length,"cm,",breadth,"cm respectively is",area,'cm²\n')
    if(Response1=='b'):
        length=eval(input("enter the value of your length:"))
        breadth=eval(input("enter the value of your breadth:"))
        perimeter= 2*(length+breadth)
        print("\nThe perimeter of the rectangle with the length and breadth",length,"cm,",breadth,"cm respectively is",perimeter,'cm\n')
    if(Response1=='c'):
        base=eval(input("enter the value of your base:"))
        height=eval(input("enter the value of your height:"))
        areaofT= 0.5*(base*height)
        print("\nThe area of the triangle with the base and height",base,"cm,",height,"cm respectively is",areaofT,'cm²\n')
    if(Response1=='d'):
        radius=eval(input("enter the value of your radius:"))
        pi=3.14
        areaofC= pi*(radius**2)
        print("\nThe area of the circle with radius",radius,"cm is",areaofC,'cm²\n')
    if(Response1=='e'):
        F= eval(input("enter the value of your farenheit:"))
        C=(5/9)*(F-32)
        print('\n',F,"Farenheit is",C,'Celsius.\n')




#else:
    #if(Response1!='a','b','c','d','e'):
       #to print this when user inputs a wrong option print('\nMAKE SURE YOUR RESPONSE IS IN UPPERCASE!!...THANK YOU')







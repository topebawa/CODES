
a,b,c=eval(input("enter number here:")),eval(input("enter number here:")),eval(input("enter number here:"))
trials=0
trials+=1
question=3
while 1==1:
    if a>b and a>c:
     print(a,"maximum value")
    if b>a and b>c:
     print(b,"maximum value")
    if c>a and c>b:
     print (c,"maximum value")
    if a<b and a<c:
     print(a,"minimum value")
    if b<a and b<c:
     print(b,"minimum value")
    if c<a and c<b:
     print (c,"minimum value")
     while (a==b) or (a==c) or (b==c):
         if (a==b==c):
             print(a,",",b,",",c,'are of equal values')
         if (a==b)<c:
            print(a,',',b,',',"are of equal values")
         if (a==b)>c:
            print(a,b,"are of equal values")
         if (a==c)<b:
            print(a,',',c,"are of equal values")
         if (a==c)>b:
            print(a,',',c,"are of equal values")
         if (b==c)<a:
            print(b,',',c,"are of equal values")
         if (b==c)>a:
            print(b,',',c,"are of equal values")

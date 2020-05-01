#list/array
name=[["game","sleep"],['girl','man','trey']]
print(len(name))
print(name)       
print(name[0][1])


#dictionary
user={'name':'stanley','email':'temibaawa@gmail.com'}
print(user['name'])
user['name']='tope'
print(user)
print(len(user))

#the difference btw them is tyaht dictionary makes use of curly brckets in listing alone/array uses squre brckets
#tuple cant be manipulated,uses a normal brcket in listing!


           #tuple
cash=('name','stanley','email',9,'temibaawa@gmail.com')
 print(cash[3])



#writing files:w-write,r-read,a-append

book=open('details.txt','w')
book.write('how tothe difference btw them is tyaht dictionary makes use of curly brckets in listing alone/array uses squre brckets')
book.close()

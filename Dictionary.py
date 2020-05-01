#list/array
#square bracket,['value','value','value',.......]
name=[["game","sleep"],['girl','man','trey']]
print(len(name))
print(name)       
print(name[0][1])




#the difference btw them is tyaht dictionary makes use of curly brckets in listing alone/array uses squre brckets
#tuple cant be manipulated,uses a normal brcket in listing!


           #tuple
#parathensis, ('value','value','value',....)
cash=('name','stanley','email',9,'temibaawa@gmail.com')
print(cash[3])


#dictionary
#curly bracket, {'key':'value'}
user={'name':'stanley','email':'temibaawa@gmail.com'}
print(user['name'])
user['name']='tope'
user['age']=3
print('--------------------------------------')
print(user)
print(len(user))
print(user.get('name'))
print(user.get('song','NOT IN DICTIONARY'))

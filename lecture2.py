print('Thanks for visiting our portal we heard there\'s an issue with your system.')

response=input('\nIs there light on your system? Reply with Y or N: ')
if(response=="Y"):
    print('come over to our office')
else:
    response2=input('Is it plugged to an AC source? Reply with Y or N: ')
    if (response2=='N'):
        print("plug it to an ac source")
    if(response2=='Y'):
        response3=input('Is it switched on? Reply with Y or N: ')
        if(response3=='N'):
            print("turn switch on")
        if (response3=='Y'):
            response4=input('Is adapter ok? Reply with Y or N: ')
            if(response4=='N'):
                print("Change Adapter")
            if(response4=='Y'):
                print('come over to our office')
                
#TROUBLESHOOTING A FAULTY SYSTEM
                
                
                
    

        

password= "pass"
username= "user"
user_name= input("Enter username:")
user_password= input("Enter password:")
if user_name==username and user_password==password:
    print("Welcome")
if user_name!=username and user_password==password:
        print("Your username is not in our database")
if user_name==username and user_password!=password:
        print ("incorrect password")
if user_name!=username and user_password!=password:
    print("wrong username and password")

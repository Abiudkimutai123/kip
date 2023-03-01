from main import User


try:
    user_name = input("Enter name \n")
    user_phone = input("Enter phone \n")
    user_email = input("Enter email \n")
    user_password = input("Enter password  \n")

    User.create(   user_name =   user_name ,    user_phone=   user_phone ,   user_email=   user_email ,    user_password =    user_password  )
    print("User Found Successfully")
except:
    print("Failed to find user")
#Write a program to prompt user to enter userid and password.
id="system"
password="kiran@123"
for i in range(1,4):
    user_id=input("Enter user_id:")
    user_password=input("Enter user_password:")
    if(id==user_id and password==user_password):
        print("welcome")
        break
    else:
        print("Reenter user_id and user_password")
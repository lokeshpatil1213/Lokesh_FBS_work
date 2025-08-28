import random

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "lokesh" and password == "1213":
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    user_input = int(input("Enter captcha: "))
    if user_input == captcha:
        print("Login Successful")
    else:
        print("Captcha Failed")
else:
    print("Invalid Credentials")

gender = (input("Enter gender (M/F):"))
age = int(input("Enter age:"))

if(gender == 'M'):
    if(age >= 21):
        print("Eligible for marriage.")
    else:
        print("Not eligible for marriage.")
else:
    if(age > 17):
          print("Eligible for marriage.")
    else:
        print("Not eligible for marriage.")
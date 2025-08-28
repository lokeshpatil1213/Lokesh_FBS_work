num = int(input("Enter a 3-digit number: "))
if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

n = int(input("Enter how many prime numbers to print: "))

count = 0 
num = 2

print("First", n,"prime numbers: ")

while (count < n):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end = ' ')
        count += 1
    num += 1
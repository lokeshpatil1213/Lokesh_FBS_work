n = int(input("Enter a number: "))
temp = n
s = 0

while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit+1):
        fact *= i
    s += fact
    temp //= 10

if s == n:
    print(n, "is a Strong Number")
else:
    print(n, "is NOT a Strong Number")

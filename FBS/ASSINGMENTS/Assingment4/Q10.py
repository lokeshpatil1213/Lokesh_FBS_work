n = int(input("Enter a number: "))
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i
if s == n:
    print(n, "is Perfect Number")
else:
    print(n, "is NOT Perfect Number")

start = int(input("Enter start: "))
end = int(input("Enter end: "))
div = int(input("Enter divisor: "))

for i in range(start, end+1):
    if i % div == 0:
        print(i, end=' ')
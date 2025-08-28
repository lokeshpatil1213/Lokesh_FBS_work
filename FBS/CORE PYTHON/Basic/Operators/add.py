'''length = int(input("Enter the length:"))
breadth = int(input("Enter the breadth:"))


area = length * breadth 
print("Area of a rectangle:",area)

n1 = int(input("Enter a number:"))
n2 = int(input("Enter a number:"))

print("Quotient", n1//n2)
print("Remainder:", n1 % n2)

P = int(input("Enter a number:"))
T = int(input("Enter a number:"))
R = int(input("Enter a number:"))

CI = P * ((1 + R / 100) ** T) - P
print("Simple Interest:", CI)

days = int(input("Enter number of days: "))
years = days // 365
weeks = (days % 365) // 7
days_left = (days % 365) % 7
print(f"{years} years, {weeks} weeks, {days_left} days")

base = float(input("Enter base: "))
height = float(input("Enter height: "))
area_triangle = 0.5 * base * height
print("Area of triangle:", area_triangle)

h = int(input("Enter hours:"))
m = int(input("Enter min:"))
s = int(input("Enter sec:"))

Total_sec = (h*3600)+(m*60)+s
print("Total seconds:", Total_sec)

num = int(input("Enter number:"))

d1= num % 10
num=num//10

d2= num % 10
num=num//10

d3= num % 10
num=num//10

print (f'd1:{d1}, d2:{d2}, d3:{d3}')
print(f'Sum of digit is:{d1+d2+d3}')

x= 10
y= 20

z=x
x=y
y=z

print(f'Before Swapping-x:{x}, y:{y}')
print(f'After Swapping-x:{x}, y:{y}')'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, ", b =", b)




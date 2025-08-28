length = float(input("Enter the length of  rectangle:"))
breadth = float(input("Enter the breadth of rectangle:"))
radius = float(input("Enter the radius of rectangle:"))

area_rectangle = length * breadth
area_perimeter = 2 * length + breadth

area_circle = 3.14*radius*radius
perimeter_circle = 2*3.14*radius

print("Area of Rectangle=",area_rectangle)
print("Perimeter of Rectangle=",area_perimeter)
print("Area of Circle=",area_circle)
print("Perimeter of Circle=",perimeter_circle)
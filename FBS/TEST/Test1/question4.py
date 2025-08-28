
area = float(input("Enter area of one wall: "))
cost_in = float(input("Enter interior wall cost per sq.m: "))
cost_ex = float(input("Enter exterior wall cost per sq.m: "))
in_walls = int(input("Enter number of interior walls: "))
ex_walls = int(input("Enter number of exterior walls: "))

total = (in_walls * area * cost_in) + (ex_walls * area * cost_ex)

print("Total painting cost =", total)

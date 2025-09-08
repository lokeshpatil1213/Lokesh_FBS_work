import math
radius = 20
length = 50
breadth = 40
cost_per_meter = 35
times = 5

perimeter = 2 * (length + breadth) + 2 * math.pi * radius
total_wire = perimeter * times
total_cost = total_wire * cost_per_meter

print(f"Total cost of fencing: {total_cost}")

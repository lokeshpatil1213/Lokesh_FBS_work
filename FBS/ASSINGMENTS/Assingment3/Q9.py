marks = [int(input(f"Enter marks of subject {i+1}: ")) for i in range(5)]
percent = sum(marks) / 5

if percent >= 75:
    print("Distinction")
elif percent >= 60:
    print("First Class")
elif percent >= 50:
    print("Second Class")
elif percent >= 35:
    print("Pass")
else:
    print("Fail")

n = int(input("how many dtudents ?"))

students = {}
for i in range(n):
    name  = input(f"Enter the name of students {i+1}:")
    marks = int(input(f"Enter marks of {name}:"))
    students[name]=marks 
    print("\n dictionary:", students)
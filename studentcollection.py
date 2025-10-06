
marks = {}

n = int(input("How many students? "))

for i in range(1, n+1):
    name = input(f"Enter the name of student {i}: ")
    score = int(input(f"Enter mark of {name}: "))
    marks[name] = score
    print("\n Current dictionary:", marks)


results = {}

for student, score in marks.items():  
    total = score                      
    average = score                    
    first_mark = score                 
    
    results[student] = {
        "Mark": score,
        "Total": total,
        "Average": average,
        "First Mark": first_mark
    }

for student, info in results.items():
    print(f"\nStudent: {student}")
    print("Mark:", info["Mark"])
    print("Total:", info["Total"])
    print("Average:", info["Average"])
    print("First Mark:", info["First Mark"])

class Student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name=name
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def total_mark(self):
        return self.mark1 +self.mark2 +self.mark3
    def avg_mark(self):
        return self.mark1 +self.mark2 +self.mark3 / 3
Students=[
    name == input("Name: "),
    Rollno = int(input("Rollno: ")),
    Mark1= int(input("Mark 1: "))
    Mark2 = int(input("Mark 2: "))
    Mark3 = int(input("Mark 3: "))
]
for stu in Students:
    Total_Mark = stu.total_mark()
    Avg_Mark = stu.avg_mark()
    print(f"{stu.name}'s total mark is {Total_Mark} and avg mark is {Avg_Mark}")



        
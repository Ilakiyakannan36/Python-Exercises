#run time
class Student:
    def __init__(self,student_rollno):
        self.student_rollno = student_rollno
        self.subjects =[]
        self.total =0
        self.avg=0
    def input_marks(self):
        print(f"Enter the marks for students")
        for i in range(1,4):
            mark = float(input(f"Subject{i}: "))
            self.subjects.append(mark)
    def cal_total(self):
        self.total = sum(self.subjects)
        self.avg = self.total/len(self.subjects)
    def disp_result(self):
        print(f"{self.student_roll}")
        print(f"{self.total},{self.avg}")
class StudentManager:
    def __init__(self,num_stud):
        self.students = [Student(i+1) for i in range (num_stud)]
    def process_student(self):
        for student in self.students:
            student.input_marks()
            student.cal_total()
    def display_all(self):
        print("Result")
        for student in self.students:
            student.display


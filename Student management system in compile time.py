class Student:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.rollno}, Name: {self.name}, Marks: {self.marks}")


class StudentManagement:
    def __init__(self):
        self.students = []

    # 1. Accept student details
    def accept(self):
        rollno = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        self.students.append(Student(rollno, name, marks))
        print("Student record added successfully.\n")

    # 2. Display all students
    def display(self):
        if not self.students:
            print("No records found.")
        else:
            print("\n--- Student Records ---")
            for student in self.students:
                student.display()
            print("------------------------\n")

    # 3. Search a student by roll number
    def search(self):
        rollno = input("Enter Roll No to search: ")
        for student in self.students:
            if student.rollno == rollno:
                print("Student Found:")
                student.display()
                return
        print("Student not found.\n")

    # 4. Delete a student record
    def delete(self):
        rollno = input("Enter Roll No to delete: ")
        for student in self.students:
            if student.rollno == rollno:
                self.students.remove(student)
                print("Student record deleted successfully.\n")
                return
        print("Student not found.\n")

    # 5. Update student details
    def update(self):
        rollno = input("Enter Roll No to update: ")
        for student in self.students:
            if student.rollno == rollno:
                print("Enter new details (leave blank to keep current value):")
                name = input(f"New Name [{student.name}]: ")
                marks = input(f"New Marks [{student.marks}]: ")

                if name:
                    student.name = name
                if marks:
                    student.marks = float(marks)

                print("Student record updated successfully.\n")
                return
        print("Student not found.\n")


# Main Program
def main():
    sm = StudentManagement()

    while True:
        print("====== STUDENT MANAGEMENT SYSTEM ======")
        print("1. Accept Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        print("=======================================")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            sm.accept()
        elif choice == '2':
            sm.display()
        elif choice == '3':
            sm.search()
        elif choice == '4':
            sm.delete()
        elif choice == '5':
            sm.update()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()

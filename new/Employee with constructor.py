class Employee:
    def __init__(self,name,hour_rate,hour_work):
        self.name=name
        self.hour_rate=hour_rate
        self.hour_work=hour_work
    def calc_salary(self):
        return self.hour_rate * self.hour_work
employees = [
    Employee("Kumar", 500,400),
    Employee("Jaya",400,50),
    Employee("Kala",600,300)

]
del employees[0]
for emp in employees:
    salary = emp.calc_salary()
    print(f"{emp.name}'s salary is ${salary}")
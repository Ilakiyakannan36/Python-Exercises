class Student:
    def read(self,roll,name):
        self.roll=roll
        self.name=name
        print("Students read:")
    def write(self):
        print("Student roll:",self.roll)
        print("Student Name:",self.name)
        print("Students write:")
s1=Student()
s2=Student()
s1.read(12,'kumar')
s1.write()
s2.read(13,'vish')
s2.write()

class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"hi {self.name}")
#if __name__ ==" __main__":
p1=Person("kumar")
p1.greet()
p2=Person("Jaya")
p2.greet()

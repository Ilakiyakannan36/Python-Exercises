class Parent:
    def __init__(self):
        print("Parent constructor called")

class Child(Parent):
    def __init__(self):
        super().__init__()  # a way to call parent method
        print("Child constructor called")

obj = Child()
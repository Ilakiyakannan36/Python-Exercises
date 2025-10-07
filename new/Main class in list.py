class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"hi {self.name}")

if __name__=="__main__":
   Human =[
       person("Kumar"),
       person("Jaya"),
       person("Kala")
       ]
for per in Human:
    print(f"{per.name}")
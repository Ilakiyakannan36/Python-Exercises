def add(a,b):
    return a+b
       
def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return a/b

print("Simple Calculator")
print("enter the choice 1.add 2.sub 3.mul 4.div")
choice=input("Enter your choice: ")
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))

if choice=="1":
    print("Result:",add(a,b))
elif choice=="2":
    print("Result:",sub(a,b))
elif choice=="3":
    print("Result:",mul(a,b))
elif choice=="4":
    print("Result:",div(a,b))
else:
    print("Invalid choice")

        

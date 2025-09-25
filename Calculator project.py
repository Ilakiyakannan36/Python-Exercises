#project 1 --> Calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return("Division by 0 is not allowed")
    return a/b
print("Enter the choice 1.Add  2.Sub  3.Mul  4.Div")
choice = int(input("Enter the choice: "))
a= int(input("Enter the a value= "))
b= int(input("Enter the b value= "))
if choice==1:
     print(add(a,b))
elif choice==2:
     print(sub(a,b))
elif choice==3:
     print(mul(a,b))
elif choice==4:
     print(div(a,b))
else :
    print("invalid")




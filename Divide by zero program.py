def div0(a,b):
    if b==0:
        return "Division by 0 is not allowed"
    return a/b
a=float(input("Enter the A value= "))
b=float(input("Enter the B value= "))
c=div0(a,b)
print("Division by 0 is not allowed")
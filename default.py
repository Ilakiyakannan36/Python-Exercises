
def add(a,b=4):# defining the module
    return a+b
a=int(input("enter the value="))
b=int(input("enter the value="))
c=add(a,b)#calling the module
print(f"result={c}")
student_name=input("enter the name of the student=")
age=input("enter the age=")
maths=int(input("enter the value of maths="))
science=int(input("enter the value of science="))
tamil=int(input("enter the value of tamil="))
total=maths+science+tamil
average=total/3
print("student name=",student_name)
print("age=",age)
print("total marks=",total)
print("average=",average)
if(average>90):
    print("grade A")
elif(average>80):
    print("grade B")
elif(average>70):
    print("grade C")
elif(average>60):
    print("just pass")
else:
    print("fail")
    



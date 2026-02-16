p=int(input("ënter the first digit"))
q=int(input("enter the second digit"))
a=p+q
b=p-q
c=p*q
d=p/q
s=input("Enter the operation (+, -, *, /): ")
if s=="+":
    print("The answer=",a)
elif s=="-":
    print("The answer=",b)
elif s=="*":
    print("The product=",c)
else:
    print("The answer=",d)

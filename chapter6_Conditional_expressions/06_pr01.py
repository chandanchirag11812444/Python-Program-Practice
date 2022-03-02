#Write a program to find the greatest of 4 numbers entered by the user
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))
d=int(input("Enter the fourth number :"))

if(a>b):
    f1=a
else:
    f1=b
if(c>d):
    f2=c
else:
    f2=d
if(f1>f2):
    print(str(f1) + " is greatest ")
else:
    print(str(f2) + " is greatest ")       


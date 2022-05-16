class Employee:
    comapany="Google"#class instance
    salary=1000
chandan=Employee()
Rajesh=Employee()
chandan.comapany="Microsoft"#obejct instance if written here will take this as priority if not then search in class instance
chandan.salary=2000

print(chandan.comapany)
print(chandan.salary)
print(Rajesh.salary)
#Now with the help of class name we can directly change the attributes of class
#
Employee.comapany="dhdhdh"
print(chandan.comapany)
print(chandan.salary)
print(Rajesh.salary)
print(Rajesh.comapany)


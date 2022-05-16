class Employee:
    company="Google"
    salary=1000

chandan=Employee()
rajni=Employee()
chandan.salary=2222
chandan.company="Mi"
# Creating instance attribute salary for both the objects
# harry.salary = 300
# rajni.salary = 400
print(chandan.company)
print(rajni.company)
# print(rajni.adress)#throws and error cause attribute adress is not present over there
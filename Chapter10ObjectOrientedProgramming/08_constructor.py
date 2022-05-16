class Employee:
    company="Google"
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
    def getDetails(self):
        print(f"The name of the person is {self.name}")
        print(f"The salary of the person is {self.salary}")
        print(f"The age  of the person is {self.age}")



chandan=Employee("chirag",1000,21)
# harry = Employee() --> This throws an error (missing 3 required positional arguments:)
chandan.getDetails() 
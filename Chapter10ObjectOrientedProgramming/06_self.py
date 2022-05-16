class Employee:
    company="google"
    def func(self):
        print(f"The company name is {self.company} and the salary is {self.salary}")


chandan=Employee()
ravindra=Employee()
chandan.salary=1000
chandan.func()
# Employee.func(chandan) same hai
# Employee.func(chandan) same hai

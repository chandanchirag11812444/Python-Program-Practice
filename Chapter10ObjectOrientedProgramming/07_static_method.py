class Employee:
    company="Google"
    def getSalary(self,signature):
        print(f" the employee working in {self.company} and the salary is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good MOrning, Sir")
    @staticmethod
    def time():
        print("The time is 9AM in the morning")
chandan=Employee()
chandan.salary=1000
chandan.getSalary("chirag")
chandan.greet()
#Employee.greet()#this we can also do
chandan.time()





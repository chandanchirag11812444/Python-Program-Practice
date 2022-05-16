#write a class calculator capable of finding the square square root and cube



class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"the number is {self.num} and the square of the nuber is {self.num **2} ")
    def squareRoot(self):
        print(f"the number is {self.num} and the square of the nuber is {self.num **0.5} ")
    def cube(self):
        print(f"the number is {self.num} and the square of the nuber is {self.num **3} ")
    @staticmethod
    def greet():
        print("Hello")
chandan=Calculator(10)
chandan.square()
chandan.squareRoot()
chandan.cube()
chandan.greet()

 
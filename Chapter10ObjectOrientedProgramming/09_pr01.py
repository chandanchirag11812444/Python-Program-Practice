#Create a class programmer for storing information of few programmers working at microsoft.class Programmer:
from click import progressbar


class Programmer:
    Company="Google"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInf(self):
        print(f"The name of the comapny is {self.Company} and the programmer is {self.name} and the product is {self.product}")

chandan=Programmer("Chandan","skype")
rajesh=Programmer("rajesh","microsoft")
chandan.getInf()
rajesh.getInf()

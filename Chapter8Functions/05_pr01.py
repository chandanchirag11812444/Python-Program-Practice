import numbers


# write a program using function to find greatest of three numbers
def numbers(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
a=numbers(10,50,30)
print(a)

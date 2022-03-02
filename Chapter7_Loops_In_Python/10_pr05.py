# write a program to find whether a given number is present in a list or not 
# from ctypes.wintypes import PINT


# number=[1,4,54,56]
# a=int(input("ENter the number "))
# if(a in number):
#     print("your number is present in list ")
# else:
#     print("Invalid number ")
names = ["harry", "shubham", "rohit", "rohan", "aditi", "shipra"]
name = input("Enter the name to check\n")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")
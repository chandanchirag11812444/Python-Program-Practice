from itertools import product


def factorial_iter(n):
    product =1
    for i in range(n):
        product =product *(i+1)
    return product

# f =factorial_iter(10)
# print(f)

def f_recursive(n):
    if n==1 or n==0:
        return 1
    return n*f_recursive(n-1)

f=f_recursive(5)
print(f)

# write arecursive function tocalculate n natural number
# 
def sumofnat(n):
    if(n<=1):
        return 1
    return n+sumofnat(n-1)



# sum=0
a=sumofnat(10)
print(a)
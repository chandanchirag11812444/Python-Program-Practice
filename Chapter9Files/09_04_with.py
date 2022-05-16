with open('onother.txt','r') as f:
    a=f.read()
print(a)
with open('onother.txt','w') as f:
    a=f.write("me")
print(a)

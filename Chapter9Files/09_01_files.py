#Use open function to read the content of the file
f=open('sample.txt','r')
# f=open('sample.txt')#By default the mode is r
# data=f.read()
data=f.read(5)
# data=f.read(5)#read first 5 characters from the file
print(data)

f.close()

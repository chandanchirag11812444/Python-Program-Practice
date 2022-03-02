# comment is defined as a text containing following keywords make a lot of money by now substitute this click this write a program to detect this
text=input("ENter yout text : ")
if("make money" in text):
    spam=True
elif("substitute this" in text):
    spam=True
elif("click this" in text):
    spam=True
else:
    spam=False
if(spam):
    print("This is a spam ")
else:
    print("This is not a spam ")

    

letter='''Dear <|NAME|>,
You are selected!
Thankyou for participating in the coding event ,we are pleased to announce your success
regards 
Bill
Date: <|DATE|>
'''
name=input("enter your name \n")
date=input("enter your date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
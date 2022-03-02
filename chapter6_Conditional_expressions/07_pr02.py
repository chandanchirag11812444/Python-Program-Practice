#Write a program to find out whether a studnet is pass or fail ,if it requires total 40% and atleast 35% in each subject to pass .assume 3 subjects and take marks as an input from the user
subj1=int(input("Enter first subject marks: "))
subj2=int(input("Enter second subject marks: "))
subj3=int(input("Enter third subject marks: "))
if(subj1<33 or subj2<33 or subj3<33):
    print("The student is failed ")
elif(subj1+subj2+subj3)/3 <40:
    print("you are fail because due to total percentage")
else:
    print("Congrats you have passed the examination")

def per(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p


marks1=[10,15,98,50]
percentage1=per(marks1) 

marks2=[80,80,98,50]
percentage2=per(marks2)

marks3=[80,70,98,50]
percentage3=per(marks3)
print(percentage1,percentage2,percentage3)
#create a class with class attribute a;create an object from it and set a directly using object a=0.Does this change the class attribute?
class Sample:
    a="Chandan"
obj=Sample()
obj.a="chirag"
print(Sample.a)
print(obj.a)

#01
class student:
    pass
student1=student()

student1.name="Ram"
student1.marks=90
print(student1.name)
print(student1.marks)#o/p:Ram, 90

#02 __init__():....
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
student1=student("Ram",90)
print(student1.name)
print(student1.marks)#o/p:Ram, 90

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
student1=student("Ram",90)
student2=student("Hari",80)
print(student1.name,student1.marks)
print(student2.name,student2.marks)#o/p:Ram 90, Hari 80

# method.......
class student:
    def display(self):
        print("Hello")
student1=student()
student1.display()#o/p:Hello
# printing students data by method..
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(self.name)
        print(self.marks)

student1=student("Ram",90)
student2=student("Hari",95)
student1.display()#o/p:Ram, 90
student2.display()#o/p: Hari, 95

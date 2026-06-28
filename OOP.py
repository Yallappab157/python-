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

# using append ....
students=[]
student1=student("Ram",90)
student2=student("Hari",95)
student3=student("Sita",80)
students.append(student1)
students.append(student2)
students.append(student3)
for student in students:
    student.display()#o/p:Ram 90,Hari 95,Sita 80

# using the loops.....
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(self.name)
        print(self.marks)
students=[]
for i in range(3):
    name=input("Enter the name of the student:")
    marks=int(input("Enter the marks of the students:"))
    student_obj=student(name,marks)
    students.append(student_obj)

for student in students:
    student.display()#o/p:yalla 92,sharana 90,sneha 93

# encapsulation.... 
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def set_marks(self,marks):
        if 0<= marks<=100:
            self.marks=marks
        else:
            print("invalid marks")
    def display(self):
        print(self.name,self.marks)

student1=student("Ram",90)
student1.display()
student1.set_marks(95)
student1.display()
student1.set_marks(-10)
student1.display()#o/p:Ram 90, Ram 95, invalid marks,Ram 95
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name,self.marks)

students=[]
student1=student("Ram",90)
student2=student("Hari",95)        
students.append(student1)
students.append(student2)

for student in students:
    student.display()#o/p:Ram 90 ,Hari 95

class student:
    def __init__(self,name,marks,branch):
        self.name=name
        self.marks=marks
        self.branch=branch
    def display(self):
        print(self.name,self.marks,self.branch)

students=[]
n=int(input("Enter the the no of the students:"))
for i in range (n):
    name=input("Enter the name of the student:")
    marks=int(input("Enter the marks of the student:"))
    branch=input("Enter the branch of the student:")

    student_obj=student(name,marks,branch)
    students.append(student_obj)

for student in students:
    student.display()
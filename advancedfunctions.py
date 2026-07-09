'''# *args:
def display(*args):
    print(args)
display(10)
display(10,20)
display(10,20,30)

def add(*numbers):
    print(sum(numbers))
add(10)
add(10,20)
add(10,20,30)

def add(*numbers):
    total=0
    for i in numbers:
        total=total+i
    print(total)
add(10)
add(10,20)
add(10,20,30)
'''
# **kwargs:
def details(**kwargs):
    print(kwargs)

details(name="Rahul",age=20)
details(name="Sneha",age=19,branch="AIML")#o/p:{'name': 'Rahul', 'age': 20},{'name': 'Sneha', 'age': 19, 'branch': 'AIML'}

def details(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)
details(name="Rahul",age=20,branch="CSE")#o/p:name : Rahul,age : 20,branch : CSE
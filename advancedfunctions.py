'''
# *args:
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

# **kwargs:
def details(**kwargs):
    print(kwargs)

details(name="Rahul",age=20)
details(name="Sneha",age=19,branch="AIML")#o/p:{'name': 'Rahul', 'age': 20},{'name': 'Sneha', 'age': 19, 'branch': 'AIML'}

def details(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)
details(name="Rahul",age=20,branch="CSE")#o/p:name : Rahul,age : 20,branch : CSE

# lambda function:
square=lambda x: x*x
print(square(5))
print(square(10))#o/p:25,100

# map():
marks=[10,20,30,40]
result=list(map(lambda x: x*2, marks))
print(result)#o/p:[20, 40, 60, 80]

# filter():
marks=[10,25,30,15,40]
result=list(filter(lambda x: x>=20,marks))
print(result)#o/p:[25, 30, 40]

# reduce():
from functools import reduce
marks=[10,20,30,40]
result=reduce(lambda x,y: x+y,marks)
print(result)# o/p:100

from functools import reduce
marks=[10,20,30,40]
result=reduce(lambda x,y: x*y,marks)
print(result)# o/p:24000

# Recursion:
def hello():
    print("Hello")
    hello()
hello()#O/P:RecursionError: maximum recursion depth exceeded

def countdown(n):
    if n==0:
        return
    print(n)
    countdown(n-1)
countdown(5)#o/p:5 ,4 , 3, 2, 1

# factorial number:
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))#o/p:120

# Iteration:
marks=[10,20,30]
it=iter(marks)
print(it)# o/p:<list_iterator object at 0x72e2584de140>

marks=[10,20,30]
it=iter(marks)
print(next(it))
print(next(it))
print(next(it))#o/p:10,20,30

marks=[10,20,30]
it=iter(marks)
print(next(it))
print(next(it))
print(next(it))
print(next(it))#o/p:StopIteration
'''
# Generators:
def numbers():
    yield 10
    yield 20
    yield 30

gen = numbers()
print(next(gen))
print(next(gen))
print(next(gen))#o/p:10,20,30

# generator using loop:
def numbers():
    for i in range(1,6):
        yield i
for value in numbers():
    print(value)#o/p:1,2,3,4,5

#Decorators:

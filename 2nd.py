'''#01
a=5
b=10
print(a+b)
c=a+b
print(c)

#02
def add(x,y):
    return x+y
print(add(10,5))

#03
Number=int(input("Enter the number:"))
def find_sqare(Num):
    return Num*Num
print(find_sqare(Number))

#04
def find_largest(a,b):
    return max(a,b)
a=int(input("enter the input 1:"))
b=int(input("Enter the input 2:"))
print(find_largest(a,b))'''

#05
Marks=int(input("Enter the marks:"))
def calculate_grade(Marks):
 if 100>=Marks>=90:
    return "A"
 elif 90>Marks>=80:
    return "B"
 elif 80>Marks>=70:
    return "C"
 else:
    return "FAIL"

print(calculate_grade(Marks))
#01 simple prog....
'''a=10
b=0
try:
    print(a/b)
except:
    print("Error")#o/p:Error

a=10
b=2
try:
    print(a/b)
except:
    print("Error")#o/p:5

try:
    print("Hello")
except:
    print("error")#o/p:Hello

#02 for input....
try:
    num=int(input("Enter the Number:"))
    print(num)
except:
    print("Enter a number!!")#o/p: if we enter 12 then prints 12,, if we enetr fgg then Enter a number!!

# no error :

try:
    a=int(input("Enter first number:"))
    b=int(input("Enetr second number:"))
    print("Result=",a/b)
except ZeroDivisionError:
    print("Cannot be divided by zero:")
print("Program completed")

# else:
try:
    a=int(input("Enter first number:"))
    b=int(input("Enetr second number:"))
    print("Result=",a/b)
except ZeroDivisionError:
    print("Cannot be divided by zero:")
else:
    print("Division is successfull")
print("Program completed")

# finally:
try:
    a=int(input("Enter first number:"))
    b=int(input("Enetr second number:"))
    print("Result=",a/b)
except ZeroDivisionError:
    print("Cannot be divided by zero:")
finally:
    print("This block always executes")
print("Program completed")
'''
# raise:
age=int(input("Enter your age:"))
if age<18:
    raise Exception("You are not eligible for vote")
print("You can vote")

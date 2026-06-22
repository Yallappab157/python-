#01 simple prog....
a=10
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
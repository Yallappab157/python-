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
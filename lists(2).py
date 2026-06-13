#06 finding even numbers:
numbers=[7,8,11,14,18]
for num in numbers:
    if num %2==0:
        print(num) # op: 8,14,18

#07 pass mrks=>40 (hw many stu passed)(distinction=>90)
marks=[90,85,95,70,92]
count=0
for mark in marks:
    if mark>=40:
        count=count+1
print("no of students passed:",count)
total=0
for mark in marks:
    if mark >=90:
        total=total+1
print("no of students got distinction:",total)
perc=(total/count)*100
print(perc) #op:no of students passed: 5,,no of students got distinction: 3,,60.0

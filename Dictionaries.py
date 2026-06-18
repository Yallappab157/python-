#01 storing marks of student and details....
student={
    "name":"Ram",
    "marks":"80"
    }
print((student["name"]))
print(student["marks"])#o/p:Ram , 80
student["marks"]="95"
print(student["marks"])#o/p:95
student["branch"]="aiml"
print(student["branch"]) #o/p:aiml

#02 using if else conditions in dictionaries...
student={
    "name":"Ram",
    "marks":80,
    "branch":"AIML"
}
print(student["marks"])
if student["marks"]>=90:
    print("Distinction")
else:
    print("Not Distinction")#o/p: 80, Not Distinction

#03
students=[
    {"name":"Ram","marks":90},
    {"name":"Shyam","marks":80},
    {"name":"Hari","marks":92},
]
print(students[0]["name"])
count=0
for student in students:
    if student["marks"]>=90:
        count=count+1
print(count)#o/p:2
print(students[0]["marks"])#o/p:90
for student in students:
    if student["marks"]>=90:
        print(student["name"])#o/p:Ram , Hari

#04
students=[
    {"name":"Ram","marks":90},
    {"name":"Shyam","marks":80},
    {"name":"Hari","marks":92},
     {"name":"Sita","marks":70},
]
count=0
for student in students:
    if student["marks"]<=90:
        count=count+1
print(count) #o/p:3
for student in students:
    if student["marks"]<=90:
        print(student["name"])#o/p:Ram,shyam,sita

#05 finding topper....
students=[
    {"name":"Ram","marks":90},
    {"name":"Shyam","marks":80},
    {"name":"Hari","marks":92},
     {"name":"Sita","marks":70},
]
top_marks=0
topper=""
for student in students:
    if student["marks"]>top_marks:
        top_marks=student["marks"]
        topper=student["name"]
print(top_marks)
print(topper)#o/p: 92,Hari
#06 finding the less scorer.......
less_marks=100
lowscorer=""
for student in students:
    if student["marks"]<less_marks:
        less_marks=student["marks"]
        lowscorer=student["name"]
print(less_marks)
print(lowscorer)#o/p: 70, Sita 
#07 for finding avg marks.....
Total=0
for student in students:
    Total=Total+student["marks"]
print(Total)
count=0
for student in students:
    count=count+1
print(count)
Avg_marks=Total/count
print(Avg_marks)#o/p:83.0(Avg_marks)

#08. finding by name...
students=[
    {"name":"Ram","marks":90},
    {"name":"Shyam","marks":80},
    {"name":"Hari","marks":92},
     {"name":"Sita","marks":70},
]
name="Hari"
marks=""
for student in students:
    if student["name"]=="Hari":
        name=student["name"]
        marks=student["marks"]
print(marks)#o/p:92
#for others.. ex...
name="Sita"
marks=""
for student in students:
    if student["name"]==name:
        name=student["name"]
        marks=student["marks"]
print(marks)#o/p:70

# 09 finding distinctions and printing names...
students=[
    {"name":"Ram","marks":90},
    {"name":"Shyam","marks":80},
    {"name":"Hari","marks":92},
     {"name":"Sita","marks":70},
]
name=""
count=0
for student in students:
    if student["marks"]>=90:
        count=count+1
        print(student["name"])
print(count)#o/p:Ram, Hari, 2
# 10 printing marks and name together...
name=""
count=0
for student in students:
    if student["marks"]>=90:
        count=count+1
        print(student["name"],student["marks"])
print(count)#o/p:Ram 90, Hari 92, 2

#11 upadating marks....
students=[
    {"name":"Ram","marks":90},
    {"name":"Shyam","marks":80},
    {"name":"Hari","marks":92},
     {"name":"Sita","marks":70},
]
for student in students:
    if student["name"]=="Shyam":
        student["marks"]=85

print(students)#o/p:{'name': 'Shyam', 'marks': 85}

for student in students:
    if student["name"]=="Sita":
        students.remove(student)
print(students)#o/p: without sita it comes

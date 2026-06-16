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
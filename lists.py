## finding who is topper using lists
#01Marks
'''Students=["ram","shyam","hari",'sita']
Marks=[90,85,95,70]
Heighest=max(Marks)
Position=Marks.index(Heighest)
print("Heighest marks:",Heighest)
print("Topper:",Students[Position])
#02
#finding averagemarks:
Marks=[90,85,95,70]
Total=sum(Marks)
length=len(Marks)
averagemarks=Total/length
print(averagemarks)

#03 
Marks=[90,85,95,70,92]
total=0
for Mark in Marks:
    if Mark>90:
        total=total+1
print(total)
Total=sum(Marks)
average_marks=Total/len(Marks)
print(Total)
print(average_marks)  #(2,432,86.4) outputs

#04 highest marks , lowest marks and difference btw them:
Marks=[90,85,95,70,92]
Marks.sort()
print(Marks)
print(Marks[-1])
print(Marks[0])
print((Marks[-1])-(Marks[0]))''' # output [70, 85, 90, 92, 95],95,70,25

#05 marks below the average :
Marks=[90,85,95,70,92]
Total=sum(Marks)
avragemarks=Total/len(Marks)
print(avragemarks)
count=0
for mark in Marks:
    if mark<avragemarks:
        count=count+1
print(count)
for mark in Marks:
    if mark<avragemarks:
        print(mark) # op:86.4,2,85,70
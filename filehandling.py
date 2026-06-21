#01 write mode....
file=open("data.txt","w")
file.write("Hello python")
file.close()
#02 read mode
file=open("data.txt","r")
data=file.read()
print(data)#o/p: Hello python
file.close()
#03 checking for other words...
file=open("data.txt","w")
file.write("Ram , Hari, Sita")
file.close()
file=open("data.txt","r")
data=file.read()
print(data)#o/p: Ram, Hari,Sita (older deleted)
file.close()

# 04 append 'a' adding new element..
file=open("data.txt","a")
file.write(" ,Yalla")

#modern code...
with open("data.txt","r") as file:
    data=file.read()
    print(data)#o/p:Ram , Hari, Sita ,Yalla

#05 read lines.....
file=open("data.txt","r")
data=file.readlines()
print(data)#o/p:['Ram , Hari, Sita ,Yalla']
file.close()

file=open("data.txt","r")
print(file.readlines())
file.close()#o/p:['Ram , Hari, Sita ,Yalla']

file=open("data.txt","r")
print(file.readline())
file.close()#o/p:Ram , Hari, Sita ,Yalla

#06 count lines....
file=open("data.txt","r")
data=file.read()
print(len(data))
file.close()
name=input("Enter the name:")
if name in data:
    print("Found")
else:
    print("Not Found")#o/p: Hari (Found), len=19
#07 len() for list...
data=["Ram","Hari","Sita"]
print(len(data))#o/p:3
data=["Ram,Hari,Sita"]
print(len(data))#o/p:1

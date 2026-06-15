#01 indexing...
name="python"
print(name[0])
print(name[-1])
print(name[1:4])
print(name[3:]) #o/p: p ,n ,yth ,hon

#02 
name="programming"
print(len(name))
print(name[0:4])
print(name[-1])
print(name[4: ]) #o/p: 11, prog, g, ramming
print(name.upper()) # PROGRAMMING
print(name.lower()) # programming
print(name.capitalize()) # Programming

#03 letter appearing , counting...
name="banana"
print(name.count("a"))
count=0
for ch in name:
    if ch=="a":
        count=count+1
print(count) #o/p: 3

#04 replace.....
word="banana"
print(word.replace("a","o"))#o/p:bonono
print(word.startswith("b"))#o/p: True
print(word.endswith("a"))#o/p: True
print(word.startswith("a"))#o/p:False

Gmail="yallappa@gmail.com"
if Gmail.endswith("@gmail.com"):
    print("Valid Gmail")
else:
    print("Not Valid") #o/p:Valid Gmail

#05 in operator....
word="python"
print("p" in word)#o/p: True
print("y" in word)#o/p:True
print("x" in word)#o/p:False

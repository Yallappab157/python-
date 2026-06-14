#01 indexing...
'''name="python"
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
print(name.capitalize()) # Programming'''

#03 letter appearing , counting...
name="banana"
print(name.count("a"))
count=0
for ch in name:
    if ch=="a":
        count=count+1
print(count) #o/p: 3


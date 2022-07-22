#dictionary comes in curly brackes {}
#dictionary pair ma chalse.. Key & Value
#key will always be unique
#any element will be accessed through key
# #value thi data access nai thay

d={1:'Vinit',2:'Amit',3:'Savan',4:'Dhruv',5:'Naresh',6:'Sonalisha',7:'Mayank',8:'Krupa',9:'Ronak'}

print(d)
print(d[3])
#print(d['Amit']) #value thi data access nai thay
d1=d.copy()
print(d1)
print(d.get(5)) # same as print(d[3])
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(3)) #dictionary ma pop function ma argument(key) enter karvi j padse
print(d)
print(d.popitem()) #by default last element remove karse
print(d)

d2={10:'Mehul',11:'Harsh',12:'Ravi',13:'Rehan'}
d.update(d2) #list ma extend hatu, dictionary ma update 6
print(d)

for i in d:
    print(i,' : ',d[i])
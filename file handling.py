# to read or write file or append another file
# file handling available in c/c++ and java
# write ma file location par nai hoy to navi create kari dese
# read and append ma file location par hovi jaruri 6
# txt format every OS par available 6.. mac,windows, ubuntu, linux that's why we use txt

file = open("tops1.txt","w") # or c:\\tops1.txt
file.write('This is file management demo using python')
file.close()
print('file written successfully')

file = open("tops1.txt","r")
print(file.read())
file.close()

file = open("tops1.txt","a")
file.write('\nFile appended')
file.close()
print('File appended successfully')

file = open("tops1.txt","r")
print(file.read())
file.close()

file = open("tops2.txt","w+") #w+ ni jem r+ pan 6 but ema file exist hovi jaruri 6.
file.write('This is w+ operation in file management using python.') #aana pa6i tarat file.read print krisu to nai print thay because cursor last position par 6
print('Cursor position : ',file.tell())
file.seek(0)
print(file.read())
file.close()
#(simple file reading and printing.)
# sequential file handling
f=open("C:\MyPython\ch8\likes.txt","r")  
for x in f:
    x=x[:-1] #starting from zero, 
#one character before last character of the line
    print(x)
#print(x, end=""), if we didn't write x=x[:-1], to remove double spacing
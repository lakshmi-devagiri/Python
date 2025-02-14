#(file reading, line by line.)
f=open("C:\MyPython\ch8\likes.txt","r")
while True:
    x=f.readline()
    if x =="":break #'' means null,can keep "" as well
    print(x,end="")
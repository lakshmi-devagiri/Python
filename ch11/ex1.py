#(Simple List used as a Stack) 
#(Stack works of LIFO principle)
def display(b) :
  for x in b :
    print (x, end=' ')
  print ("\n")
a = [105, 6, 7, 9.4 ]
print (a)
display(a)
a.pop()
display(a)
a.append(5) # like pushing
display(a)
a.insert(2,6.6)
display(a)
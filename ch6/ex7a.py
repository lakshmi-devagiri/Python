# input a sentence and print its words vertically
sentence=input("Enter a sentence:")
s = sentence.split(" ")
n = len(s)
for i in range(0,n):
    print(s[i])
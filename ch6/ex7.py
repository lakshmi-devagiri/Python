# input a sentence and print its words vertically
sentence=input("Enter a sentence:")
n=len(sentence)
for i in range(0,n):
    if(sentence[i]== " "):
       print()
    else:
        print(sentence[i], end="")   
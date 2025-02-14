# input a word and print if it is a palindrome or not
word =input("enter a word:")
n=len(word)
pal=True
for i in range(0,n):
    if(word[i] != word[n-1-i]):
        pal = False
if pal == True:
    print("Palindrome")
else:
    print("Not palindrome") 

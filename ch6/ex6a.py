# input a word and print if it is a palindrome or not
word =input("enter a word:")
word1 = word[::-1]

if word == word1:
    print("Palindrome")
else:
    print("Not palindrome")
    
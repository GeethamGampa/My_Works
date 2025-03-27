# Program to check given input is Palindrome or not

def ispalindrome(s):
    return s==s[::-1]
s = input("Enter a string or a number: ")

if ispalindrome(s):
    print("Is a Palindrome")
    
else:
    print("Not a Palindrome")

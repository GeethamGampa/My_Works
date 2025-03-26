#Calculate the factorial of a number 
#taking input from the user

def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial

a = int(input("Enter a number: "))
print(f"The factorial of {a} is {factorial(a)}") 
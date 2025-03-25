#Calculator using functions

def calculator(first, second, operator):
    if operator == "+":
        return first + second
    elif operator == "-":
        return first - second
    elif operator == "*":
        return first * second
    elif operator == "%":
        return first % second
    elif operator == "/":
        return first / second
    else:
        return "Invalid Operator"


first = int(input("Enter the 1st number: "))
second = int(input("Enter the 2nd number: "))
operator = input("Enter the operator (+ - * % /): ")

# Call the function and print the result
print("Result:", calculator(first, second, operator))

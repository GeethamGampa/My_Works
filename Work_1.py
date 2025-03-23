# create a calculator which is having a = 5, b = 6

first = input("Enter the 1st number : ")
second = input("Enter the 2nd number : ")
operator = input("Enter the operator(+ - * % /): ")

first = int(first)
second = int(second)

if operator == "+":
    print (first + second)
elif operator == "-":
    print (first - second)
elif operator == "*":
    print (first * second)
elif operator == "%":
    print (first % second)
elif operator == "/":
    print (first / second)
    
else:
    print("Invalid Operator")
    
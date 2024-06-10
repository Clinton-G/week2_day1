def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Invalid Imput, Try Again"
    else:
        return num1 / num2

def calculator():
    while True:
        #had to get this input part from the internet cause i couldnt find any way to do it
        num1, num2, type = input("Enter num1, num2, then the type seperated by spaces (+, -, *, /): ").split()

        num1 = float(num1)
        num2 = float(num2)

        if type == '+':
            print("Result:", add(num1, num2))
        elif type == '-':
            print("Result:", subtract(num1, num2))
        elif type == '*':
            print("Result:", multiply(num1, num2))
        elif type == '/':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid Input, Try Again")

        choice = input("Go Again? (yes/no): ")
        if choice.lower() != 'yes':
            break

        # if choice == "no":
        #     print("Have a Good Day")
calculator()
#WeekEnd Assignment 2
#Question : To create a calculator
#Code:
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error! Division by zero."

def floor_divide(x, y):
    if y != 0:
        return x // y
    else:
        return "Error! Division by zero."

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulus")
    print("7. Floor Division")
    
    choice = input("Enter choice(1/2/3/4/5/6/7): ")
    
    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
        elif choice == '5':
            print(f"The result is: {exponentiate(num1, num2)}")
        elif choice == '6':
            print(f"The result is: {modulus(num1, num2)}")
        elif choice == '7':
            print(f"The result is: {floor_divide(num1, num2)}")
    else:
        print("Invalid Input")

calculator()


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def exponential(a,b):
    return a**b

def remainder(a,b):
    return a%b

while True:
    print("nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponential (Power)")
    print("6. Modulus (Remainder)")
    print("7. Exit")

    choice = input("Choose an operation (1-7): ")

    if choice == '7':
        print("Exiting the calculator. Goodbye!")
        break  # Exit the loop

    if choice in ['1', '2', '3', '4','5','6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", exponential(num1, num2))
        elif choice == '6':
            print("Result:", remainder(num1, num2))
    else:
        print("Invalid input! Please enter a number between 1 and 7.")



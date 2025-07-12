def calculator():
    """Simple calculator with basic arithmetic operations"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ").strip()
        
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation. Please use +, -, *, or /")
            
    except ValueError:
        print("Please enter valid numbers only")

if __name__ == "__main__":
    calculator()
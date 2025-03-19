# Basic Calculator Program  

# Function to perform the calculation  
def calculate(num1, num2, operation):  
    if operation == '+':  
        return num1 + num2  
    elif operation == '-':  
        return num1 - num2  
    elif operation == '*':  
        return num1 * num2  
    elif operation == '/':  
        if num2 != 0:  
            return num1 / num2  
        else:  
            return "Error: Division by zero is not allowed."  
    else:  
        return "Error: Invalid operation."  

# User input  
try:  
    number1 = float(input("Enter the first number: "))  
    number2 = float(input("Enter the second number: "))  
    operation = input("Enter the operation (+, -, *, /): ")  
    
    result = calculate(number1, number2, operation)  
    
    if isinstance(result, str):  # Check if the result is an error message  
        print(result)  
    else:  
        print(f"{number1} {operation} {number2} = {result}")  
except ValueError:  
    print("Error: Please enter valid numbers.")  
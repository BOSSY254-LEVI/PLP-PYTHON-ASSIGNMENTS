num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("CHOOSE AN OPERATION (+, -, *, /): ")
if operation == "+":
    result = float(num1) + float(num2)
elif operation == "-":
    result = float(num1) - float(num2)
elif operation == "*":
    result = float(num1) * float(num2)
elif operation == "/":
    result = float(num1) / float(num2) 
    if float(num2) != 0:
        result = float(num1) / float(num2)
    else:
        result = "Error: Division by zero is not allowed."

print(f"THE RESULT OF YOUR OPERATION IS: {result}")


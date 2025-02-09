operator = input("Enter an operator (+, -, *, /, %, **): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
elif operator == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "Error: Division by zero"
elif operator == "**":
    result = num1 ** num2
else:
    result = "Invalid operator"

print(f"{num1} {operator} {num2} = {result}")
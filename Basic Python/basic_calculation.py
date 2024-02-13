# Addition
result_addition = 5 + 3
print("Addition:", result_addition)

# Subtraction
result_subtraction = 10 - 4
print("Subtraction:", result_subtraction)

# Multiplication
result_multiplication = 6 * 7
print("Multiplication:", result_multiplication)

# Division
result_division = 20 / 5
print("Division:", result_division)

# Exponentiation
result_exponentiation = 2 ** 3
print("Exponentiation:", result_exponentiation)

# Modulo (remainder)
result_modulo = 10 % 3
print("Modulo:", result_modulo)



# Take user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Take user input for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation based on user input
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Check if the denominator is not zero
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero is not allowed."
else:
    result = "Error! Invalid operation."

# Print the result
print("Result:", result)

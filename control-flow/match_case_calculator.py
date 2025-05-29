def calculator(num1, num2, operation):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2 if num2 != 0 else "Cannot divide by zero"
        case _:
            return "Invalid operation"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

print(f"The result is {calculator(num1, num2, operation)}")


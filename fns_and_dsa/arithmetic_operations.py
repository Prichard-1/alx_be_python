ithmetic_operations.py
def perform_operation(num1:float, num2:float, operation):
    """performs basic arithmetic operations based on operation parameter."""
    if operation=="add":
        return num1 + num2
    elif operation=="subtract":
        return num1 - num2
    elif operation=="multipy":
        return num1 * num2
    elif operation=="devide"
         if num2==0:
             return "error: Division by zero is not allowed."
         return num1/num2
    else:
        return "Error: Invad operation. Choose from 'add', 'subtract', 'multiply', or 'devide'."
    

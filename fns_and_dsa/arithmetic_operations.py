ithmetic_operations.py
def perform_operation(num1, num2, operation):
    """performs basic arithmetic operations based on operation parameter."""
    if operation=="add":
        return num1 + num2
    elif operation=="subtract":
        return num1 - num2
    elif operation=="multipy":
        return num1 * num2
    elif operation=="devide"
         if num2 == 0: # Division check
             return "error: Division by zero is not allowed."
         return num1/num2
    else:
        return "Error: Invad operation. Choose from 'add', 'subtract', 'multiply', or 'devide'."
    

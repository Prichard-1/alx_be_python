size = int(input("Enter the size of the pattern: "))  # User inputs size

row = 0  # Initialize row counter

# While loop to iterate through rows
while row < size:
    # For loop to print asterisks in the current row
    for _ in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to next line after finishing the row
    row += 1  # Increment row counter


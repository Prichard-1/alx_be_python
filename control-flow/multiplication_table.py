# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
print(f"\nMultiplication table for {number}:")  # Use 'number' (not 'numbers')
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")


# Get input from the user and convert to an integer
num = int(input("Enter a number for the multiplication table: "))

# Print a header for the table
print(f"--- Multiplication Table for {num} ---")

# Use a for loop to iterate from 1 to 10
for i in range(1, 11):
    # Calculate the product
    product = num * i
    # Print the result using an f-string
    print(f"{num} x {i} = {product}")

n = int(input("Enter the number of rows (half of the diamond): "))

# Print the upper half of the diamond
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Print the lower half of the diamond
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

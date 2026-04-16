# Performs basic list operations and prints even numbers
# 1. Create a list of 6 numbers
numbers = [10, 25, 3, 8, 15, 20]

# 2. Print the list
print("List:", numbers)

# 3. Find max and min
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# 4. Calculate sum
print("Sum:", sum(numbers))

# 5. Print only even numbers
print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)
# Array (List) Example in Python

numbers = [10, 20, 30, 40, 50]

# Print whole array
print("Array:", numbers)

# Access elements
print("First element:", numbers[0])
print("Second element:", numbers[1])

# Add element
numbers.append(60)
print("After append:", numbers)

# Update element
numbers[2] = 35
print("After update:", numbers)

# Remove element
numbers.remove(40)
print("After remove:", numbers)

# Loop through array
print("All elements:")
for num in numbers:
    print(num)

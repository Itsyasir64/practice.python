def second_largest(numbers):
    largest = second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

nums = [10, 20, 4, 45, 99]
print("Second largest:", second_largest(nums))

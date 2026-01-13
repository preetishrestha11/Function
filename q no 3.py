def calculate_sum(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

# Example usage
result = calculate_sum(1, 5)
print(result)

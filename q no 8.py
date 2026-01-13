def skip_two(lst):
    result = []
    for i in range(1, min(len(lst), 12), 3):
        result.append(lst[i])
    return result

# Example usage
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(skip_two(data))

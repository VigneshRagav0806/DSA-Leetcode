def min(arr):
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

print(min([1, 2, 3, 4, 5]))  # Output: 1
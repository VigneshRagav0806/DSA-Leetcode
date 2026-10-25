def removeDuplicates(arr):
    n = len(arr)
    if n <= 1:
        return arr

    # Start from the second element
    idx = 1  

    result = []
    result.append(arr[0])

    for i in range(1, n):
        if arr[i]!= arr[i - 1]:
            result.append(arr[i])
    return result
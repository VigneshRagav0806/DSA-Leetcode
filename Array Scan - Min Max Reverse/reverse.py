def reverse(arr):
    for i in range(len(arr)-1, -1, -1):
         print(arr[i], end=" ")


print(reverse([1, 2, 3, 4, 5]))  # Output: 5 4 3 2 1 none
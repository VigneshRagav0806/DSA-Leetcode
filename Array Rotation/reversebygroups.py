def reverse_groups(arr, k):
    n = len(arr)

    for i in range(0,n,k):
        left = i
        right = min(i + k - 1, n - 1)

        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
print(reverse_groups(arr, k))

"""The code reverses the elements of an array in groups of size k. 
It iterates through the array in steps of k, and for each group, it reverses the 
elements by swapping them from the ends towards the center. 
If the last group has fewer than k elements, it still reverses that group. 
The output for the given input will be [3, 2, 1, 6, 5, 4, 8, 7].
"""
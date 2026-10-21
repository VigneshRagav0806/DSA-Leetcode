def binarysearchforinsertion(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

binarysearchforinsertion([1, 3, 5, 6], 5)
"""
The function returns the index where the target should be inserted to maintain the sorted order.
Time complexity is O(log n) and space complexity is O(1).
"""
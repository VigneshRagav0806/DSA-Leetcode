def containsduplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(containsduplicates([1, 2, 4, 4, 5]))  # Output: True


"""Brute force solution is a double for loop that checks if any element matches with another element O(n^2)."""
"""Two pointer solutions are not applicable here because the array isn't sorted."""
"""We can use a set to track the repetitive element. If element in array is already in set, we get true"""
"""We can compare the length of the array and that of the set. If not equal, there is some duplicate element in the array."""
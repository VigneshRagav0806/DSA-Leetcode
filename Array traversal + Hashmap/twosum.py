
def twosum(nums: list[int], target: int) -> list[int]:
    map = {}
    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in map:
            return [map[complement], i]
        else:
            map[nums[i]] = i

    return [-1, -1]

print(twosum([2, 7, 11, 15], 9))  # Output: [0, 1]

"""Brute force solution is a double for loop that checks if any element matches with another element O(n^2)."""
"""Two pointer solutions are not applicable here because the array isn't sorted."""
"""We can use a hashmap to store the index of each element. For each element, we check if the complement (target - current element) exists in the hashmap. If it does, we return the indices of the two elements."""
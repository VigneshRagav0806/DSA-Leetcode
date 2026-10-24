class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        result = []
        seen = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in seen:
                result.append(i)
        return result

"""
The solution employs a set to eliminate the duplicates in the input list
empty output list is declared
We traverse each element if each i not in the set, the index is added to the resulting list
We return the list
Time Complexity : O(n)
"""
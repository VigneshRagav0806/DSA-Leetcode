class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        sum=n*(n+1)//2
        actual=0
        for i in range(n):
            actual+=nums[i]
        return sum-actual

"""
The length of the list is found, Formula n*(n+1)//2 is applied to find a sum of natural numbers
Using for loop, found the sum of list elements
We return difference in both sums
Time Complexity : O(n)
"""
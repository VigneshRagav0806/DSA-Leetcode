class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        sqr=[]
        for num in nums:
            sqr.append(num*num)

        return sorted(sqr)

"""
The solution is a for loop that square each element and appends to sqr array
we return a sorted sqr array
"""
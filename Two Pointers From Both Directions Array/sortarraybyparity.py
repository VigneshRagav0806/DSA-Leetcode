class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        
        return nums

"""
The two pointer method uses a left variable in the first position and moves across the elements and swaps the elements 
pushes the variable up one position, if the element is
"""
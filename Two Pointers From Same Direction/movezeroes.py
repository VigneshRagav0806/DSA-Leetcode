class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        for high in range(len(nums)):
            if nums[high]!=0:
                nums[low],nums[high]=nums[high],nums[low]
                low+=1
            
"""
The code implements two pointer method to move zeroes to the right.
The fast pointer on encountering a non-zero number will swap its value with slow pointer value. Then the slow pointer will move one step.
O(n) Time Complexity.
"""
            



        
def singlenumber(nums):
    map_count = {}
    for num in nums:
        if num in map_count:
            map_count[num]+=1
        else:
            map_count[num]=1

    for n in map_count:
        if map_count[n]==1:
            return n

print(singlenumber([2,2,1]))  # Output: 1

"""Brute force solution is a double for loop that checks if any element matches with another element O(n^2)."""
"""The written solution implements a dictionary to count occurrences of each element in the array. The element with a count of 1 is returned as the single number."""
"""Other method is to use a xor operation. XOR of a number with itself is 0 and XOR of a number with 0 is the number itself. So if we take XOR of all the numbers, the result will be the single number."""
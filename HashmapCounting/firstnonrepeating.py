def firstnonrepeating(nums):
    map = {}
    for num in nums:
            if num in map:
                map[num]+=1
            else:
                map[num]=1
    for num in map:
            if map[num]==1:
                return num
    return -1

print(firstnonrepeating([1, 2, 3, 2, 1, 4, 5])) # Output: 3

"""
The solution uses a map to count occurrences of each number and return the first number with 1 occurence
"""
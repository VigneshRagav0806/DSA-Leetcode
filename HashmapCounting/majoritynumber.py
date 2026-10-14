def majoritynumber(arr):
    map = {}
    for num in arr:
        if num in map:
            map[num]+=1
        else:
            map[num]=1

    for m in map:
        if map[m] > len(arr)//2:
            return m
    return -1

print(majoritynumber([1, 2, 3, 2, 2, 2, 5, 4, 2])) # Output: 2

""" 
This solution implements an empty map to count occurrences of each number in the input array.
It is mentioned in the question that the majority number appears more than n/2 times, where n is the array length.
If map[m] where m is the number and map[m] is the count, is greater than len(arr)//2, then m is the majority number.

Optimal solution : To sort the array and return the nums[len(nums)//2]. It beats 100% of the submissions and 0ms runtime.

"""
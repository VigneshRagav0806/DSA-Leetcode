def firstbadversion(n):
    left,right=1,n
    while left<=right:
        mid=left+(right-left)//2
        if isBadVersion(mid):
            right=mid-1
        else:
            left=mid+1
    return left

"""
The code can not be run as the boolean function was an inbuilt function in leetcode. If the bad version is found then the 
left pointer is returned as the first bad version. The time complexity of the code is O(logn) and the space complexity is O(1).
"""
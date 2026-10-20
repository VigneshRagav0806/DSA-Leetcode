def guesshigherorlower(n):
    low=1
    high=n
    while low<=high:
        mid=low+((high-low)//2)
        answer=guess(mid)
        if answer==0:
            return mid
        elif answer<0:
            high=mid-1
        else:
            low=mid+1


"""The question in leetcode has a built in api called guess(num) which takes the mid as input and return a number from -1,0,1.
-1 means the number is lower than the mid, 0 means the number is equal to mid and 1 means the number is higher than mid.
The code can not be effectively run and only to demonstrate the logic of binary search to find the number.
Time complexity is O(logn)
"""
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        distinct=set()
        n=len(nums1)
        m=len(nums2)
        if n>m:
            bigger=n
            list1=nums1
            list2=nums2
        else:
            bigger=m
            list1=nums2
            list2=nums1
        
        for i in range(bigger):
            if list1[i] in list2:
                distinct.add(list1[i])
            

        return list(distinct)

    """
    The solution compares the two lists and assigns the greater size to a common variable and the list of that size to a common variable
    We traverse the bigger list
    If the bigger list elements appears in the smaller list, then we add it to a set (we omit duplicates)
    We return the set as a list
    Time Complexity : O(n)
    """
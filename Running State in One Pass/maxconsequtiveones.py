def maxconsequtiveones(nums):
    res = 0
    count = 0
    for n in nums:
        if n==0:
            count =0
        else:
            count+=1

        if count>res:
            res=count
    return res

print(maxconsequtiveones([1,1,0,1,1,1])) #Output 3
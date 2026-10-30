def twosumsorted(arr,target):
    map={}
    for i in range(len(arr)):
        complement=target-arr[i]
        if complement in map:
            map[complement]+=1
            return [arr[i],map[complement]]
        else:
            map[complement]=1
    return [-1,-1]

se=twosumsorted([2,5,7,9],9)
print(se)

    
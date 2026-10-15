def sumarray(arr):
    sum = 0
    for i in range(len(arr)):
        sum+=arr[i]

    return sum

print(sumarray([1,2,3,4,5])) #Output 15
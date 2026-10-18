def rotatearray(arr):
    n = len(arr)
    b=[0]*n
    b[n-1]=arr[0]
    for i in range(1,n):
        b[i-1]=arr[i]

    return b

res = rotatearray([1,2,3,4,5])
print(res)

"""The code executes rotating an array by 1 position to the right. Manually the first element is moved to the last position
and all other elements are shifted one position to the left. The output of the code is [2, 3, 4, 5, 1] which is the rotated array."""
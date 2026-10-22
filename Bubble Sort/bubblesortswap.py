def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr

res=bubblesort([64, 34, 25, 12, 22, 11, 90])
print(res)
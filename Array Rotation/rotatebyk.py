def rotate(A,k):
    n = len(A)
    k=k%n
    reverse(A,0,n-1)
    reverse(A,0,k-1)
    reverse(A,k,n-1)
    return A

def reverse(A,left,right):
    while left<right:
        A[left],A[right]=A[right],A[left]
        left+=1
        right-=1

A=[1,2,3,4,5,6,7]
k=24
res = rotate(A,k)
print(res)

"""
k=k%n is used to handle large k values. Like k=24 can be reduced to k=3 since k=3 output and k=24 output are the same.
It also reduces how many times we reverse the array.
"""
def perfectsquare(n):
    low=0
    high=n
    while low<=high:
        mid=low+((high-low)//2)
        sqr=mid*mid
        if sqr==n:
            return True
        elif sqr<n:
            low=mid+1
        else:
            high=mid-1
    return False

n=int(input("Enter a number"))
res=perfectsquare(n)
print(res)
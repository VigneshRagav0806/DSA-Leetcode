def sqrt(num):
    low, high = 0, num
    while low <= high:
        mid = low + ((high-low)//2)
        sqr = mid*mid
        if sqr == num:
            return mid
        elif sqr < num:
            low = mid +1
        else:
            high = mid-1
    return high

res = sqrt(8)
print(res)
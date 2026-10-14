def countfrequency(arr):
    map = {}
    for num in arr:
        if num in map:
            map[num]+=1
        else:
            map[num]=1

    return map

print(countfrequency([1, 2, 3, 2, 1, 4, 5])) # Output: {1: 2, 2: 2, 3: 1, 4: 1, 5: 1}

"""The solution is to only count occurrences of each number in the input array and return the map of frequencies"""
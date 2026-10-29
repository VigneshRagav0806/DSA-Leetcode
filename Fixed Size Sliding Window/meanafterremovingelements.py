def trimMean(arr: list[int]) -> float:
    arr.sort()

    n = len(arr)
    remove = n // 20

    total = 0
    count = 0

    for i in range(remove, n - remove):
        total += arr[i]
        count += 1

    return total / count

n = trimMean([0, 2, 2, 2, 2, 2, 2, 2, 1])
print(n)

# Sort the array in ascending order
# Calculate the number of elements to remove from each end (5%)
# Initialize the sum and count of the remaining elements
# Traverse the array, excluding the smallest and largest 5% of elements
# Add each remaining element to the total sum
# Increment the count of remaining elements
# Return the mean of the remaining elements
# Call the function with the input array and store the result
# Print the calculated mean

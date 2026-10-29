def maxsubarraysum(arr,k):
    sum_arr=0
    for i in range(k):
        sum_arr+=arr[i]

    max_sum=sum_arr
    for r in range(k,len(arr)):
        sum_arr=sum_arr+arr[r]-arr[r-k]
        max_sum=max(sum_arr,max_sum)
    return max_sum

sum_array_average=maxsubarraysum([1,12,-5,-6,50,3],4)
print(sum_array_average)

# Sort the array in ascending order
# Calculate the number of elements to remove from each end (5%)
# Initialize the sum and count of the remaining elements
# Traverse the array, excluding the smallest and largest 5% of elements
# Add each remaining element to the total sum
# Increment the count of remaining elements
# Return the mean by dividing the total sum by the count
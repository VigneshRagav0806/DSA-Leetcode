def maxsumaverage(arr,k):
    sum_arr=0
    for i in range(k):
        sum_arr+=arr[i]

    max_sum=sum_arr
    for r in range(k,len(arr)):
        sum_arr=sum_arr+arr[r]-arr[r-k]
        max_sum=max(sum_arr,max_sum)
    return max_sum/k


sum_array_average=maxsumaverage([1,12,-5,-6,50,3],4)
print(sum_array_average)

# Calculate the sum of the first k elements to form the initial window
# Store the initial window sum as the maximum sum
# Start sliding the window from index k to the end of the array
# Remove the element leaving the window and add the new element
# Update the maximum sum if the current window sum is greater
# Return the maximum average by dividing the maximum sum by k
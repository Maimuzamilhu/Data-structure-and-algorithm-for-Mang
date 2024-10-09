# Function to Use Inversion Count
def mergeSort(arr, n):
	# A temp_arr is created to store
	# sorted array in merge function
	temp_arr = [0]*n
	return helper(arr, temp_arr, 0, n-1)


def helper(arr, temp_arr, left, right):

	inv_count = 0

	if left < right:

		mid = (left + right)//2

    ## Left subtree inversion count
		inv_count += helper(arr, temp_arr,
								left, mid)
    ## Right subtree inversion count
		inv_count += helper(arr, temp_arr,
								mid + 1, right)

    ## after merge/combine inversion count
		inv_count += mergeProcedure(arr, temp_arr, left, mid, right)
	return inv_count


def mergeProcedure(arr, temp_arr, left, mid, right):
	i = left	 # Starting index of left subarray
	j = mid + 1 # Starting index of right subarray
	k = left	 # Starting index of to be sorted subarray
	inv_count = 0

	# Conditions are checked to make sure that
	# i and j don't exceed their
	# subarray limits.

	while i <= mid and j <= right:

		# There will be no inversion if arr[i] <= arr[j]
		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:
			# Inversion will occur.
			temp_arr[k] = arr[j]
			inv_count += (mid-i + 1)
			k += 1
			j += 1

	# Copy the remaining elements of left
	# subarray into temporary array
	while i <= mid:
		temp_arr[k] = arr[i]
		k += 1
		i += 1

	# Copy the remaining elements of right
	# subarray into temporary array
	while j <= right:
		temp_arr[k] = arr[j]
		k += 1
		j += 1

	# Copy the sorted subarray into Original array
	for i in range(left, right + 1):
		arr[i] = temp_arr[i]

	return inv_count


# Driver Code
arr = [70, 50, 60, 10, 20, 30, 80, 15]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are", result)
def partition(arr, low, high):
    pivot = arr[low]  # Pivot is chosen as the first element
    i = low + 1  # Start from the second element

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:  # Compare each element with the pivot
            arr[i], arr[j] = arr[j], arr[i]  # Swap smaller element with arr[i]
            i += 1

    # Place the pivot in its correct position
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1  # Return the final index of the pivot


def quick_select(arr, low, high, k):
    if low <= high:
        # Partition the array around the pivot (first element)
        pivot_index = partition(arr, low, high)

        # If the pivot is in its kth position, return the pivot
        if pivot_index == k - 1:
            return arr[pivot_index]
        # If the pivot index is greater than k-1, recurse on the left subarray
        elif pivot_index > k - 1:
            return quick_select(arr, low, pivot_index - 1, k)
        # If the pivot index is less than k-1, recurse on the right subarray
        else:
            return quick_select(arr, pivot_index + 1, high, k)
    return None


# Example usage
arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 2
result = quick_select(arr, 0, len(arr) - 1, k)
print(f"The {k}th smallest element is {result}")

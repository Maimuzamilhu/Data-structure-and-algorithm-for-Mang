# Time complexity : O(n^2)
def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        # Min Index
        min_inx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_inx]:
                min_inx = j
        ## Swap happend after every pass
        arr[i], arr[min_inx] = arr[min_inx], arr[i]
    return  arr

# Driver code
arr = [70, 56, 23, 19, 25, 37, 48]
result = selectionsort(arr)
print("Array after using selection sort is:", result)
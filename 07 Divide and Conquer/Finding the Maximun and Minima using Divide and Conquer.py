## Recurrence Relation : T(n) = 2T(n/2) + c
## Using master's theorem: T(n) = O(n)
## Method Definition of MaxandMin function
def findMaxandMin(arr, i, j):
    ## small problem - c
    ## single element condition
    if i == j:
        max_val = arr[i]
        min_val = arr[i]
    ## two element condition
    elif i == j - 1:
        if arr[i] < arr[j]:
            max_val = arr[j]
            min_val = arr[i]
        else:
            max_val = arr[i]
            min_val = arr[j]
    ## big problem -> n > 2
    else:
        ## Divide and Conquer approach
        ## 1. Divide - c
        mid = i + (j-i)//2
        ## 2.Recursion -> Conquer - 2T(n/2)
        max_1, min_1 = findMaxandMin(arr, i, mid)
        max_2, min_2 = findMaxandMin(arr, mid+1, j)
        ## 3. Combine
        ## To find the final maxima - c
        if max_1 < max_2:
            max_val = max_2
        else:
            max_val = max_1
        ## To find the final minima
        if min_1 < min_2:
            min_val = min_1
        else:
            min_val = min_2
    return max_val, min_val

## Driver code
arr = [20, 39, 45, 65, 21, 44, 89, 92]
## i indicates the starting index
i = 0
## j indicates the ending index
j = len(arr) - 1
## function calling
max_val, min_val = findMaxandMin(arr, i, j)
print('Maximum and Minimum value in the array is', max_val, min_val)
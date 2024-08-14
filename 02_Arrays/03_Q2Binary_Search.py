## Binary Search Algorithm using recursion
## function definition
def binarySearch(arr, x, i, j):
    while i <= j:
        mid = i + (j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:

            i = mid+1
        else:
          j = mid-1
    return -1

## Driver code
arr = [20, 30, 40, 50, 60, 70, 80, 90]
x = 80
i = 0
j = len(arr) - 1
## function calling
result = binarySearch(arr, x, i, j)
print("Searching element is present at the location:",result)
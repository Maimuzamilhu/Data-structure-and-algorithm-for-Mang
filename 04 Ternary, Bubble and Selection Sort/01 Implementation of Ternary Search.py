

def ternarysearch(arr, i, j, key):
    while i<=j:
        mid1 = i + (j-i)//3
        mid2 = j - (j-i)//3

        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return  mid2
        if key < arr[mid1]:
            return ternarysearch(arr, i, mid1-1, key)
        elif key > arr[mid2]:
            return ternarysearch(arr, mid2+1, j, key)
        else:
            return  ternarysearch(arr, mid1+1, mid2-1, key)
    return  -1


# Driver code
arr = [20, 25, 47, 56, 63, 65, 79, 82]
i = 0
j = len(arr) - 1
key = 79
result = ternarysearch(arr, i, j, key)

print(result)
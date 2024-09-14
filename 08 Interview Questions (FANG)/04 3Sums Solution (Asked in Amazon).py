def Closest(arr, x):
    # Assuming the difference between elements in list are not larger then target*1000000
    Closest_Sum = abs(x * 1000000)
    arr.sort()

    # arr[i] will move till len(arr)-2
    # because arr[right] already exists on len(arr) - 1
    for i in range(len(arr) - 2):

        left = i + 1
        right = len(arr) - 1

        while left < right:

            # If the sum is more closer than
            # the current closest sum
            sumVal = arr[i] + arr[left] + arr[right]
            if (abs(x - sumVal) < abs(x - Closest_Sum)):
                Closest_Sum = sumVal

            elif sumVal > x:
                right -= 1

            else:
                left += 1

    return Closest_Sum


# Driver code
arr = [-1, 2, 3, -4]
target = 5
print(Closest(arr, target))
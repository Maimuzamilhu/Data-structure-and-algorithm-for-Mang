def perfectsquare(x):
    if x < 1:
        return False
    left = 1
    right = x
    while left <= right:
        mid = left+(right-left)//2
        square = mid*mid
        if square == x:
            return True
        elif square < x:
            left =mid+1
        else:
            right=mid-1
    return  False

print(perfectsquare(16))
print(perfectsquare(16))
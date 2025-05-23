def sqrt(x):
    if x == 0:
        return 0
    left = 1
    right = x
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

# Test cases
print(sqrt(4))  # Should output: 2
print(sqrt(8))  # Should output: 2
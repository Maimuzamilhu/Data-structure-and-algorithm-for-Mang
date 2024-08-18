## Time complexity: O(n)
## Two pointer approach

def two_sum(arr, target_sum):
    l = 0  # Left pointer
    r = len(arr) - 1  # Right pointer

    while l < r:
        current_sum = arr[l] + arr[r]
        if current_sum == target_sum:  # Check if the sum matches the target
            return l, r  #
        elif current_sum < target_sum:  # If the sum is less, move the left pointer to the right
            l += 1
        else:  # If the sum is greater, move the right pointer to the left
            r -= 1
    return -1, -1

# Derived
arr = [20, 40, 60, 80, 90, 120, 240]
target_sum = 210
result = two_sum(arr, target_sum)
print(result)

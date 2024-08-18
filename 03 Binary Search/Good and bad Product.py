def first_bad_version(versions):
    left = 0
    right = len(versions) - 1

    while left < right:
        mid = left + (right - left) // 2
        if versions[mid] == 1:
            right = mid  # Search in the left half
        else:
            left = mid + 1  # Search in the right half

    return left


# Test Case
versions = [0, 0, 0, 1, 1, 1, 1, 1, 1]
result = first_bad_version(versions)
print(f"The first bad version is at index: {result}")
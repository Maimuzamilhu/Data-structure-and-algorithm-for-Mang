def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    n = len(nums)
    if n % 2 == 0:
        mid = n // 2
        return (nums[mid] + nums[mid - 1]) / 2
    else:
        return nums[n // 2]


## Driver code
nums1 = [1, 2]
nums2 = [3, 4]
result = findMedianSortedArrays(nums1, nums2)
print(result)

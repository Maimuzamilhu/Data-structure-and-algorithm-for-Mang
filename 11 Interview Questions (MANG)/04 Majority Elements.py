## Majority Element
## Method definition
## TC = O(n)
## SC = O(n)
from collections import Counter
def majorityElement(nums):
    counts = Counter(nums)
    print(counts)
    return max(counts.keys(), key = counts.get)

## Driver code
nums = [2, 2, 1, 1, 1, 2, 2]
result = majorityElement(nums)
print("Majority element in an array is:",result)
## TC - O(n)
## SC - O(1)
## Method definition of findCandidate
def findCandidate(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

## Method definition of isMajorityElement
def isMajorityElement(nums, candidate):
    cnt = 0
    size = len(nums)
    for i in range(size):
        if nums[i] == candidate:
            cnt += 1
    if cnt > size/2:
        return 1
    else:
        return 0

## Method definition of printMajorityElement
def printMajorityElement(nums):
    cand = findCandidate(nums)
    if isMajorityElement(nums, cand):
        print("Majority element is:", cand)
    else:
        print("No Majority element exists in an array")

## Driver code
nums = [3, 2, 3, 4, 3]
printMajorityElement(nums)
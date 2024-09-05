from  collections import  Counter
import  heapq

def topkfrequent(arr,k):
    if k == len(arr):
        return  set(arr)
    count = Counter(arr)
    heapq.nlargest(k,count.keys() , key = count.get)

# Driver Code
arr = [1,1,1,1,2,2,2,2,3]
k = 2 #top most 2 frequent element

result = topkfrequent(arr,k)
print(result)

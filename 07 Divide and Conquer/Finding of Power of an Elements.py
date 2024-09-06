## method definition
def findPowerOfElement(a, n):
    ## small problem
    if n == 1:
        return a
    elif n == 0:
        return 1
    else:
        ## big problem
        ## 1. Divide
        mid = n//2
        ## 2. Conquer
        b = findPowerOfElement(a, mid)
    ## 3. Combine
    result = b * b
    if n % 2 == 0:
        return result
    return result * a

## Driver code
a = 2
n = 16
## function calling
result = findPowerOfElement(a,n)
print("The power of an element is:", result)
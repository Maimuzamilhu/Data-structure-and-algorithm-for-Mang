def possibilities(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        ## recursion
        return possibilities(n-1) + possibilities(n-2)
## Driver code
n = 8
result = possibilities(n)
print(result)
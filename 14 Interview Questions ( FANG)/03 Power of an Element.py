def myPow(x, n):
  if n == 0:
    return 1
  ## this is the major logic
  elif n < 0:
    x = 1/x
    n = -n
    return myPow(x, n)
  elif n == 1:
    return x
  else:
    ## Divide
    mid = n // 2
    ## conquer
    b = myPow(x, mid)
    result = b * b
    ## combine
    if n % 2 == 0:
      return result
    else:
      return result * x

## Driver code
x = 2.00000
n = -2
result = myPow(x, n)
print(result)
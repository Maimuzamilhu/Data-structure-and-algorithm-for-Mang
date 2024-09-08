# Using Slope formula
def colinear(x1, x2, x3, y1, y2, y3):
    # y2-y1/x2-x1 == y3-y2/x3-x2 if both slops are equal then it should be colinear

    if ((y2-y1)*(x3-x1) == (y3-y2)*(x2-x1)):
        print("Yes it's Linear")
    else:
        print("its not")



# Driver Code
x1, x2, x3, y1, y2, y3 = 1, 1, 1, 6, 0, 9
colinear(x1, x2, x3, y1, y2, y3)

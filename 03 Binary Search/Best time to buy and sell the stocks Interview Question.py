## function definition
## time complexity: O(n)
def findMaxProfit(price):
    min_price = float("inf")
    max_price = 0

    for i in range(len(price)):
        if price[i] < min_price:
            min_price = price[i]
        elif price[i] - min_price > max_price:
            max_price = price[i] - min_price
    return max_price



# Deriver code
price = [7, 4, 5, 3, 6, 16 ]
max_profit_value = findMaxProfit(price)
print("The Max profit of this stock is " , max_profit_value)


"""For Visualization paste this code into this website : https://pythontutor.com/render.html#mode=display"""

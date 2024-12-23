from collections import Counter
products = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt']

products.sort()
# Dict and count---> counter is usded for frequency
productCount = dict(Counter(products))
print(productCount)

max = 0
req_frequncy= []
for i in productCount:
    if max<= productCount[i]:
        max = productCount[i]
for key, value in products_count.items():
    if max == value:
        rqd_product.append(key)
print(rqd_product[-1])
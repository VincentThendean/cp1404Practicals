"""
Get item_number
Loop item_number times
    get price
    print price
Sum all price
if sum > 100
    discount 10%
print price
"""

item_number = int(input("Number of items: "))
while item_number < 0:
    print('Invalid number of items!')
    item_number = int(input("Number of items: "))
itemSum = float(0)
for i in range(item_number):
    itemPrice = float(input(f"Price of item {i + 1} : "))
    itemSum += itemPrice
if itemSum >= 100:
    itemSum *= 0.9
print(f"Total price for {item_number} items is $", end='')
print(float(round(itemSum, 2)))

"""
CP1404 Prac 1
"""
salesRevenue = int(input("Enter Sales: $"))

while salesRevenue >= 0:
    if salesRevenue < 1000:
        print(f'Bonus: {salesRevenue*0.1}')
        print(15 / 3 + 2 * 4)
    elif salesRevenue >1000:
        print(f'Bonus: {salesRevenue*0.15}')
    else:
        print(f'Bonus: 300')
    salesRevenue = int(input("Enter Sales: $"))
print("Neg Number")

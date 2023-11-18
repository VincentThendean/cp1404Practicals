for i in range(1, 21, 2):
    print(i, end=' ')

print("\na)", end=' ')
for i in range (0, 101, 10):
    print(i, end=' ')

print("\nb)", end=' ')
for i in range (20):
    print(20-i, end=' ')

print("\nc)", end=' ')
starC = int(input('Number of Stars: '))
for i in range (starC):
    print('*', end='')

print("\nd)")
for i in range(starC):
    for j in range(i+1):
        print('*', end='')
    print("")
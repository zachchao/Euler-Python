
last = 1
n = 1
sumOfDiagonals = 1
while last < 1001 * 1001:
    n += 2
    # In the nxn square, we add the corners
    # which will be equal to the last corner + n-1
    lowerCorner = last + n - 1
    higherCorner = last + (4 * (n - 1))
    sumOfDiagonals += 2 * (lowerCorner + higherCorner)
    last = higherCorner

print(sumOfDiagonals)

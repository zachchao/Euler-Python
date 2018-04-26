def isRightTriangle(a, b, c):
    return a**2 + b**2 == c**2


def amtOfTriangles(perim):
    listOfSets = []
    for a in range(1, perim - 2):
        for b in range(1, perim - a - 1):
            c = perim - a - b
            if isRightTriangle(a, b, c):
                if {a, b, c} not in listOfSets:
                    listOfSets.append({a, b, c})
    return len(listOfSets)


maxAmt = 0
maxPerim = 0

for perim in range(12, 1000, 12):
    amt = amtOfTriangles(perim)
    if amt > maxAmt:
        maxAmt = amt
        maxperim = perim
        print(str(perim) + " perimeter has " + str(amt))

print(maxPerim)


triangulars = [1]
pentagonals = [1]
hexagonals = [1]


def isTriangular(n):
    while triangulars[-1] < n:
        generateNextTriangular()
    if n in triangulars:
        return True
    return False


def generateNextTriangular():
    n = len(triangulars)
    triangulars.append(n * (n + 1) / 2)


def isPentagonal(n):
    while pentagonals[-1] < n:
        generateNextPentagonal()
    if n in pentagonals:
        return True
    return False


def generateNextPentagonal():
    n = len(pentagonals)
    pentagonals.append(n * (3 * n - 1) / 2)


def isHexagonal(n):
    while hexagonals[-1] < n:
        generateNextHexagonal()
    if n in hexagonals:
        return True
    return False


def generateNextHexagonal():
    n = len(hexagonals)
    hexagonals.append(n * (2 * n - 1))


notFound = True
i = 144
while(notFound):
    if isPentagonal(i * (2 * i - 1)):
        notFound = False
        print(i * (2 * i - 1))
    i += 1

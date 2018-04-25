
triangulars = [1]
alphabet = list(" ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def isTriangular(n):
    while triangulars[-1] < n:
        generateNextTriangular()
    if n in triangulars:
        return True
    return False


def generateNextTriangular():
    n = len(triangulars)
    triangulars.append(n * (n + 1) / 2)


def triangleWord(word):
    total = sum([alphabet.index(i) for i in list(word)])
    return isTriangular(total)


triangularWords = 0
with open("Problem42.txt") as file:
    for word in file.read().replace('"', "").split(","):
        if triangleWord(word):
            triangularWords += 1

print(triangularWords)

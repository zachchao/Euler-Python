
# All pandigital products must be a 2 digit number
# times a 3 digit number because 99*999 is 5 of the
# alloted 9 numbers and leaves us only 4 left
# and is already a 5 digit number

allNums = {i for i in range(1, 10)}


def pandigitalProduct(a, b):
    theseNums = []
    digits = list(str(a)) + list(str(b)) + list(str(a * b))
    for digit in digits:
        theseNums.append(int(digit))
    if len(theseNums) != 9:
        return False
    theseNums = set(theseNums)
    return allNums == theseNums


allPanProducts = set()
for a in range(999):
    for b in range(9999):
        if pandigitalProduct(a, b):
            allPanProducts.add(a * b)

print(sum(list(allPanProducts)))

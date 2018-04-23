
# First generate all abundant numbers
def generateAllAbundant(limit):
    abundants = []
    for i in range(1, limit):
        if abundant(i):
            abundants.append(i)
    return abundants


# A number is abundant if the sum of its
# factors exceeds the number itself
def abundant(n):
    factors = factorsOf(n)
    sumOfFactors = sum(factors)
    return sumOfFactors > n


# To generate abundant numbers we must be able
# to generate all factors of a number
def factorsOf(n):
    factors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(int(n / i))
    factors.remove(n)
    return list(factors)


allAbundants = generateAllAbundant(28123)

total = 0

sumOfTwoAbundants = set()

for abundant1 in allAbundants:
    for abundant2 in allAbundants:
        if abundant1 + abundant2 >= 28123:
            break
        sumOfTwoAbundants.add(abundant1 + abundant2)

sumOfTwoAbundants = list(sumOfTwoAbundants)

total = 0
for i in range(28123):
    total += i

for i in sumOfTwoAbundants:
    total -= i

print(total)
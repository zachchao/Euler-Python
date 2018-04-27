
primeFactorsList = [{None}, {None}, {2},
    {3}, {2}, {5}, {2, 3}, {7}, {2}, {3}]
for i in range(10, 150000):
    primeFactorsList.append({None})


def sieveOfE(limit):
    # True means it is prime
    sieve = [True for i in range(limit)]
    sieve[0] = False
    sieve[1] = False
    for i in range(len(sieve)):
        if sieve[i]:
            for j in range(i * 2, limit, i):
                sieve[j] = False
    return sieve


def primeFactors(n):
    if sieve[n]:
        primeFactorsList[n] = {n}
        return primeFactorsList[n]
    if primeFactorsList[n] != {None}:
        return primeFactorsList[n]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if primeFactorsList[n // i] == {None}:
                primeFactors(n // i)
            divisibleSet = set(primeFactorsList[n // i])
            divisibleSet.add(i)
            primeFactorsList[n] = divisibleSet
            return primeFactorsList[n]


def generatePrimeList(limit):
    primes = []
    for i in range(limit):
        if sieve[i]:
            primes.append(i)
    return primes


limit = 1000000
sieve = sieveOfE(limit)
primes = generatePrimeList(limit)
window = 4

for i in range(1000, 150000 - 5):
    first = len(primeFactors(i))
    second = len(primeFactors(i + 1))
    third = len(primeFactors(i + 2))
    fourth = len(primeFactors(i + 3))
    if first == window and second == window and third == window and fourth == window:
        print(i, i + 1, i + 2, i + 3)
        break



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


def primeAndTwiceASquare(n):
    for prime in primes:
        if prime > n:
            return False
        if isInt(((n - prime) / 2) ** 0.5):
            return True
    return False


def isInt(n):
    return n == int(n)


limit = 1000000
sieve = sieveOfE(limit)
primes = []
for i in range(limit):
    if sieve[i]:
        primes.append(i)

for i in range(9, 10000, 2):
    if not sieve[i]:
        if not primeAndTwiceASquare(i):
            print(i)
            break

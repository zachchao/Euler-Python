
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


def permutationsOf(a, b, c):
    return set(list(str(a))) == set(list(str(b))) == set(list(str(c)))


limit = 10000
sieve = sieveOfE(limit)
primes = []
for i in range(limit):
    if sieve[i]:
        primes.append(i)

for prime in primes:
    if prime > 999 and prime < 3340:
        b = prime + 3330
        c = prime + 6660
        if sieve[b] and sieve[c]:
            if permutationsOf(prime, b, c):
                print(prime, b, c)

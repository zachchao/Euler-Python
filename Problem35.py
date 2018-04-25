
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


# Apparently we don't count numbers that have 0 in them
def circularPrime(n):
    #Check if contains 0s
    for digit in list(str(n)):
        if int(digit) == 0:
            return False
    for i in range(len(str(n))):
        rotation = int(str(n)[1:] + str(n)[0])
        if not sieve[rotation]:
            return False
        n = rotation
    return True


limit = 1000000
sieve = sieveOfE(limit)
primes = []
for i in range(limit):
    if sieve[i]:
        primes.append(i)

amtOfCircularPrimes = 0
for i in primes:
    if circularPrime(i):
        amtOfCircularPrimes += 1
        print(i)

print(amtOfCircularPrimes)

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


def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isPandigital(n):
    allNums = {str(i) for i in range(1, 8)}
    return set(list(str(n))) == allNums


# n can only be 7 at the max because if the sum of
# a numbers digits is divisible by three then
# so is the number, 9-pandigital and 8=pandigital
# numbers will always be divisble by 3 and therefore
# not prime
limit = 7654321
sieve = sieveOfE(limit)
primes = []
for i in range(limit):
    if sieve[i]:
        primes.append(i)

for prime in primes[::-1]:
    if isPandigital(prime):
        print(prime)
        break

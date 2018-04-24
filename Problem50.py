
def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


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


# Returns the first prime which can be written a
# a sum of primes of window length
def primeSearch(window):
    for i in range(1000 - window):
        windowSum = primeSum(primes[i:i + window])
        if windowSum == -1:
            pass
        else:
            if isPrime(windowSum):
                print(i)
                return [windowSum, window]
    return -1


def primeSum(primeList):
    total = 0
    for prime in primeList:
        total += prime
        if total > 1000000:
            return -1
    return total


limit = 1000000
sieve = sieveOfE(limit)
primes = []
for i in range(limit):
    if sieve[i]:
        primes.append(i)

window = 6
answer = 41
while window < 1000:
    answer = primeSearch(window)
    print(answer)
    window += 1

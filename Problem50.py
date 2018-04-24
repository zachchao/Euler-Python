
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


limit = 1000
sieve = sieveOfE(limit)
primes = []
for i in range(limit):
    if sieve[i]:
        primes.append(i)


# Returns the first prime which can be written a
# a sum of primes of window length
def primeSearch(window):
    for i in range(limit - window):
        windowSum = sum(primes[i:i + window])
        if isPrime(windowSum):
            return windowSum
    return -1


window = 6
answer = 41
while answer != -1:
    answer = primeSearch(window)
    print(answer)
    window += 1



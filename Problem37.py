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


def isTruncatable(n):
    if n < 10:
        return False
    return leftTruncatable(n) and rightTruncatable(n)


def leftTruncatable(n):
    if n == 0:
        return True
    if sieve[n]:
        return leftTruncatable(n % 10**(len(str(n)) - 1))
    return False


def rightTruncatable(n):
    if n == 0:
        return True
    if sieve[n]:
        return rightTruncatable(n // 10)
    return False


limit = 1000000
sieve = sieveOfE(limit)
total = 0
for i in range(limit):
    if sieve[i]:
        if isTruncatable(i):
            total += i

print(total)




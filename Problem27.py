
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

sieve = sieveOfE(100000)

def consecutiveNs(a, b):
    n = 0
    while True:
        if sieve[n**2 + a*n + b]:
            n += 1
        else:
            return n - 1


best = 0
bestA = 1
bestB = 41

for a in range(-1000, 1000):
    for b in range(1000):
        if sieve[b]:
            consec = consecutiveNs(a, b)
            if consecutiveNs(a, b) > best:
                best = consec
                print(consec, a, b)
                bestA = a
                bestB = b

print(bestA, bestB, bestA*bestB)

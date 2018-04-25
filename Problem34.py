
factorials = [1, 1]


def factorial(n):
    if len(factorials) - 1 < n:
        factorials.append(n * factorial(n - 1))
        return factorials[n]
    return factorials[n]


def digitFactorial(n):
    total = 0
    for i in list(str(n)):
        total += factorial(int(i))
    return total == n


sumOfDigitFactorials = 0
for i in range(3, 2540160):
    if digitFactorial(i):
        sumOfDigitFactorials += i

print(sumOfDigitFactorials)

factorials = [1, 1]


def factorial(n):
    if len(factorials) - 1 < n:
        factorials.append(n * factorial(n - 1))
        return factorials[n]
    return factorials[n]


def C(n, r):
	return factorial(n) // (factorial(r) * factorial(n - r))


values = 0
for n in range(22, 101):
	for r in range(2, n):
		if C(n, r) > 1000000:
			values += 1
print(values)
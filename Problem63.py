
powerFulDigitCount = 0

for j in range(100):
	i = 1

	limit = 10 ** j
	while True:
		powerDigits = i ** j
		if len(str(powerDigits)) == j:
			powerFulDigitCount += 1
		if powerDigits >= limit:
			break
		i += 1

print(powerFulDigitCount)

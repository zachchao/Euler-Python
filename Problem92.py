squareDigitChainList = [0, 1] + [0] * 10000000
squareDigitChainList[89] = 89

def squareDigits(n):
	total = 0
	for i in list(str(n)):
		total += int(i) ** 2
	return total


def squareDigitChain(n):
	if squareDigitChainList[n] != 0:
		return squareDigitChainList[n]
	return squareDigitChain(squareDigits(n))


answer = 0
for i in range(1, 10000000):
	squareDigitChainList[i] = squareDigitChain(i)
	if squareDigitChainList[i] == 89:
		answer += 1
print(answer)

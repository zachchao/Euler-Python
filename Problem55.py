def isPalindrome(n):
	return str(n) == str(n)[::-1]


def isLychrel(n):
	for i in range(50):
		n += int(str(n)[::-1])
		if isPalindrome(n):
			return True
	return False


total = 0
for i in range(10000):
	if not isLychrel(i):
		total += 1
print(total)

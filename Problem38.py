
def isPandigital(n):
	if len(str(n)) < 9 or len(str(n)) > 9:
		return False
	return set(list(str(n))) == {str(i) for i in range(1,10)}


biggest = 0
for i in range(1000, 9999):
	s = ""
	for j in range(1, 3):
		s += str(i * j)
	if isPandigital(int(s)):
		if int(s) > biggest:
			biggest = int(s)

print(biggest)

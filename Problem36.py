
def decToBinary(n):
    return int(bin(n)[2:])


def isPalindrome(n):
    n = str(n)
    firstHalf = n[: int(len(n) / 2)]
    secondHalf = n[int(len(n) / 2) + len(n) % 2:]
    return firstHalf == secondHalf[::-1]


def doubleBasePalindrome(n):
    binary = decToBinary(n)
    return isPalindrome(n) and isPalindrome(binary)


total = 0
for i in range(999999):
    if doubleBasePalindrome(i):
        total += i

print(total)


def digitSum(a, b):
    return sum([int(i) for i in(list(str(a ** b)))])


maxSum = 0
for a in range(10, 100):
    for b in range(10, 100):
        thisDigitSum = digitSum(a, b)
        if thisDigitSum > maxSum:
            maxSum = thisDigitSum

print(maxSum)
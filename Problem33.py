
def isDigitCanceling(n, d):
    frac1 = n / d
    c = commonDigit(n, d)
    if c == -1:
        return False
    if n % 10 == 0 or d % 10 == 0:
        return False
    # after removal
    listN = list(str(n))
    listN.remove(c)
    n2 = int(listN[0])
    listD = list(str(d))
    listD.remove(c)
    d2 = int(listD[0])
    frac2 = n2 / d2
    return frac1 == frac2


def commonDigit(n, d):
    if str(n)[0] in list(str(d)):
        return str(n)[0]
    if str(n)[1] in list(str(d)):
        return str(n)[1]
    return -1


ns = 1
ds = 1
for d in range(10, 100):
    for n in range(10, d):
        if isDigitCanceling(n, d):
            print(str(n) + " / " + str(d))
            ns *= n
            ds *= d

print(str(ns) + " / " + str(ds))
print(ns / ds)

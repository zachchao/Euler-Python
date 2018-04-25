
def increasing(n):
    last = -1
    for current in str(n):
        if int(current) < last:
            return False
        last = int(current)
    return True


def decreasing(n):
    last = 10
    for current in str(n):
        if int(current) > last:
            return False
        last = int(current)
    return True


notBouncy = 0
bouncy = 0
i = 1

while True:
    if not increasing(i) and not decreasing(i):
        bouncy += 1
    else:
        notBouncy += 1
    if int((bouncy / (notBouncy + bouncy)) * 100) == 99:
        print(i)
        break
    else:
        i += 1

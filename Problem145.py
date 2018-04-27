
def reversible(n):
    if n % 10 == 0:
        return False
    reverse = int(str(n)[::-1])
    for i in [int(i) for i in list(str(n + reverse))]:
        if i == 0 or i % 2 == 0:
            return False
    return True


total = 0
for i in range(1000):
    if reversible(i):
        total += 1
print(total)


def recurringDecimal(n):
    # When we divide we get the integer and a remainder
    # to go further and get decimals we then divide the
    # remainder by n, when we get the same remainder that
    # we have before, we are in a loop
    pastRemainders = []
    remainder = 10 % n
    repeated = False
    length = 1
    if remainder == 0:
        return length
    while not repeated:
        pastRemainders.append(remainder)
        remainder = remainder * 10 % n
        if remainder in pastRemainders:
            repeated = True
            return length
        length += 1
        
maxLength = 0
for i in range(2, 1000):
    length = recurringDecimal(i)
    if length > maxLength:
        maxLength = length
        print(i)
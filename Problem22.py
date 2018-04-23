
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

with open("Problem22.txt", "r") as f:
    names = f.read().replace('"', "").split(",")
    # Sort alphabetically
    names = sorted(names)

def nameValue(name, index):
    # Sum up the letters
    total = 0
    for letter in list(name):
       total += alphabet.index(letter) + 1
    return total * index

total = 0
for name in names:
    total += nameValue(name, names.index(name) + 1)

print(total)
from collections import Counter
compare = lambda u, v, w, x, y, z: Counter(u) == Counter(v) == Counter(w) == Counter(x) == Counter(y) == Counter(z)
for i in range(150000):
	if compare(list(str(i)), list(str(i*2)), list(str(i*3)), list(str(i*4)), list(str(i*5)), list(str(i*6))):
		print(i, i*2, i*3, i*4, i*5, i*6)
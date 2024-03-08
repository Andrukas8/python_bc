# Args packs all parameters into a tuple

def add(*stuff):
	sum = 0
	for i in stuff:
		sum += i
	return sum

print(add(1,2,3,4,5))


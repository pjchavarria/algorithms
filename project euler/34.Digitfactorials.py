fact = []
def init():
	fact.append(1)
	for i in range (1, 10):
		fact.append(fact[i - 1] * i)

def num_to_digits(n):
	sz = len(str(n))
	digits = []
	for i in range(0, sz):
		digits.append(n % 10)
		n = n / 10
	return list(reversed(digits))

def solve():
	suma = 0
	for i in range(10, 409114):
		array = num_to_digits(i)
		s = 0
		for l in range(len(array)):
			s += fact[array[l]];	
		if s == i:
			print i
			suma += i
	return suma

def main():
	init()
	res = solve()
	print "SUMA: ", res
main()

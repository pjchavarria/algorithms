#Link: https://leetcode.com/problems/add-binary/
class Solution:
	def int2bin(self, i):
		if i == 0:
			return "0"
		s = ""
		while i:
			if i & 1 == 1:
				s = "1" + s
			else:
				s = "0" + s
			i /= 2
		return s

	def addBinary(self, a, b):
		n1 = int(a, 2)
		n2 = int(b, 2)
		n3 = n1 + n2
		return self.int2bin(n3)

def main():
	s = Solution()
	res = s.addBinary('0', '0')
	print res
main()
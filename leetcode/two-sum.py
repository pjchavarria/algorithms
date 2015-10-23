class Solution:
	# @return a float
	def findMedianSortedArrays(self, A, B):
		return self.getMedium(sorted(A + B))

	def getMedium(self, A):
		lenA = len(A)
		if lenA != 0:
			if lenA % 2 == 0:
				return (A[lenA/2-1]+ A[lenA/2])/2.0
			else:
				return A[lenA/2]
		else:
			return 0


print Solution().findMedianSortedArrays([],[1,2]), 1.5
print Solution().findMedianSortedArrays([],[1]), 1
print Solution().findMedianSortedArrays([1,2],[1,2]), 1.5
print Solution().findMedianSortedArrays([1,2,3],[1,2]), 2
print Solution().findMedianSortedArrays([1],[2,3,4]), 2.5
class Solution:
	def coverPoints(self, A, B):
		count = 0
		for i in range(len(A)-1):
			count += max(abs(A[i+1] - A[i]),abs(B[i+1] - B[i]))
		return count


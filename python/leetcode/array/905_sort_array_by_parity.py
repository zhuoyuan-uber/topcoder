"""
905. Sort Array By Parity (Easy)

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for item in A:
        	if item % 2 == 0:
        		even.append(item)
        	else:
        		odd.append(item)
        for item in odd:
        	even.append(item)
        return even


if __name__ == "__main__":
	a = Solution()
	print(a.sortArrayByParity([3,1,2,4]))
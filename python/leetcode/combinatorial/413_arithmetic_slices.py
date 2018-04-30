'''
413. Arithmetic Slices (Medium)

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
'''

class Solution(object):
  def numberOfArithmeticSlices(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    n = len(A)
    if n <= 2: return 0
    i = 0 
    result_ = []
    while(i<n):
      if i+2<n and A[i]+A[i+2]==2*A[i+1]:
        begin = i
        end = i+2
        diff = A[i+1]-A[i]
        while(end<n):
          if end+1<n and A[end+1]-A[end]==diff:
            end += 1
          else:
            break
        result_.append(end-begin+1)
        i = end + 1
      else:
        i += 1
    result = 0
    for item in result_:
      result += (item-1)*(item-2)/2
    return result


if __name__ == '__main__':
  a = Solution()
  print a.numberOfArithmeticSlices([1,2,3,4])
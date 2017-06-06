"""
507. Perfect Number (Easy)

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""
import math

class Solution(object):
  def checkPerfectNumber(self, num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 1: return False
    tmp_set = set([1])
    for i in range(2, int(math.sqrt(num)+1)):
      if num % i == 0:
        tmp_set.add(i)
        tmp_set.add(num/i)
    if sum(tmp_set) == num:
      return True
    else:
      return False

  def solution2(self, num):
    if num == 1: return True
    base = 2
    result = base * (base*2-1)
    while(num > result):
      base **= 2
      result = base * (base*2-1)
    return result == num

if __name__ == '__main__':
  a = Solution()
  for i in range(1, 10000):
    if a.checkPerfectNumber(i):
      # if a.solution2(i):
      print i

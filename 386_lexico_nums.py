'''
386. Lexicographical Numbers

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
'''

class Solution(object):
  def lexicalOrder(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    digit = self.decide_digit(n)
    result = []
    for i in range(1,10):
      tmp_result = self.helper(i, digit)
      for item in tmp_result:
        if item <= n: result.append(item)
    return result

  def helper(self, k, n):
    # everything in alphabetical order, with <= n digits
    if n == 1:
      return [k]
    else:
      tmp_result = self.helper(k, n-1)
      result = []
      for item in tmp_result:
        result.append(item)
        if self.decide_digit(item) == n-1:
          for i in range(10):
            result.append(item*10+i)
      return result
       
  def decide_digit(self, k): 
    # decide how many digits does k have
    n = 0
    while(k!=0):
      k /= 10
      n += 1
    return n 

if __name__ == '__main__':
  a = Solution()
  # print a.helper(1, 3)
  print a.lexicalOrder(100)

"""
645. Set Mismatch (Easy)

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""
import collections

class Solution(object):
  def findErrorNums(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ctr = dict(collections.Counter(nums))
    result = []
    for k in ctr.keys():
      if ctr[k] == 2:
        result.append(k)
        break
    # missing one
    n = len(nums)
    s = n*(n+1)/2 - (sum(nums) - result[0])
    result.append(s)
    return result

if __name__ == '__main__':
  a = Solution()
  print a.findErrorNums([1,2,2,4])
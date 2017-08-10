'''
315. Count of Smaller Numbers After Self (Hard)

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
'''
class TreeNode(object):
  def __init__(self, val):
    self.val = val
    self.cnt = 0
    # record number of nodes on the left
    self.dup = 1
    self.left = None
    self.right = None

class Solution(object):
  def countSmaller(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums = nums[::-1]
    if len(nums) == 0: return False
    result = [0]
    root = TreeNode(nums[0])
    for i in range(1, len(nums)):
      tmp = self.find(root, nums[i], 0)
      result.append(tmp)
    result = result[::-1]
    print root.val, root.cnt, root.dup
    return result

  def find(self, node, num, cnt):
    if node.val == num:
      node.dup += 1
      return cnt + node.cnt
    elif num > node.val: # inserted number is larger than node value
      cnt += node.cnt + node.dup
      if node.right is not None:
        return self.find(node.right, num, cnt)
      else:
        new_node = TreeNode(num)
        node.right = new_node
        return cnt
    else: # inserted number is smaller than node value
      node.cnt += 1
      if node.left is not None:
        return self.find(node.left, num, cnt)
      else:
        new_node = TreeNode(num)
        node.left = new_node
        return cnt

if __name__ == "__main__":
  a = Solution()
  print a.countSmaller([6,0, 3,2,2,6,1])

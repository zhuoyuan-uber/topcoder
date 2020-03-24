"""
993. Cousins in Binary Tree (Easy)

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        q = [root]
        if root is None or root.val in [x, y]:
            return False
        while len(q) > 0:
            newq = []
            vals = set()
            while len(q) > 0:
                n = q.pop()
                if n.left is not None:
                    newq.append(n.left)
                    vals.add(n.left.val)
                if n.right is not None:
                    newq.append(n.right)
                    vals.add(n.right.val)
                if n.left is not None and n.right is not None:
                    if n.left.val in [x, y] and n.right.val in [x, y]:
                        return False
            if x in vals and y in vals:
                return True
            q = newq
        return False
        
"""
998. Maximum Binary Tree II (Medium)

We are given the root node of a maximum tree: a tree where every node has a value greater than any other value in its subtree.

Just as in the previous problem, the given tree was constructed from an list A (root = Construct(A)) recursively with the following Construct(A) routine:

If A is empty, return null.
Otherwise, let A[i] be the largest element of A.  Create a root node with value A[i].
The left child of root will be Construct([A[0], A[1], ..., A[i-1]])
The right child of root will be Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
Return root.
Note that we were not given A directly, only a root node root = Construct(A).

Suppose B is a copy of A with the value val appended to it.  It is guaranteed that B has unique values.

Return Construct(B).

 

Example 1:



Input: root = [4,1,3,null,null,2], val = 5
Output: [5,4,null,1,3,null,null,2]
Explanation: A = [1,4,2,3], B = [1,4,2,3,5]
Example 2:


Input: root = [5,2,4,null,1], val = 3
Output: [5,2,4,null,1,null,3]
Explanation: A = [2,1,5,4], B = [2,1,5,4,3]
Example 3:


Input: root = [5,2,3,null,1], val = 4
Output: [5,2,4,null,1,3]
Explanation: A = [2,1,5,3], B = [2,1,5,3,4]
 

Note:

1 <= B.length <= 100
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # case 0: empty
        if root is None:
            return TreeNode(val)
        # case 1: larger than everything
        if val >= root.val:
            node = TreeNode(val)
            node.left = root
            return node
        # case 2:
        if root.left is None:
            root.left = TreeNode(val)
        elif root.right is None:
            root.right = TreeNode(val)
        else:
            if val < root.left.val and val < root.right.val:
                _ = self.insertIntoMaxTree(root.left, val)
            elif val >= root.left:
                node = TreeNode(val)
                node.left = root.left
                root.left = node
            else:
                node = TreeNode(val)
                node.right = root.right
                root.right = node
        return root

    def solve2(self, root, val):
        if root and root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        node = TreeNode(val)
        node.left = root
        return node


if __name__ == "__main__":
    a = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n5.left, n5.right = n2, n4
    n2.right = n1
    a.insertIntoMaxTree(n5, 3)


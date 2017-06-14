import collections
import sys

# String
s = 'abccccxxx'
s.find('x') # first occurence
s.lower()
s.upper()
s.count('aaa') # count non-overlapping
s.split()
s.replace()
' '.join(s_list) # will remove extra spaces!!! :)


# Array sorting
arr.sort(key= lambda x: x[0])
arr.sort(key= lambda x: (x[0],x[1]))
arr.sort(key= len)
reversed(arr)

# stack
# implemented as a list
stack = [1]
stack.pop() # rightmost

# Queue
queue = collections.deque()
queue.append(1) # append rightmost
queue.appendleft(1) # append leftmost
queue.clear()
queue.count(1) # how many times 1 appears
queue.pop() # pop from rightmost
queue.popleft() # pop from left

# Priority Queue
# Implemented by Heap

# heap

# iterator

# string technqiues:
s_split = s.split(' ') # split into a list of substr
s_strip = s.strip() # strip multi-spaces into one
s_strip = s.replace(' ', '') # stripping all spaces

# maxint, minint
print sys.maxint
print -sys.maxint

# Trie
class TrieNode():
  def __init__(self):
    self.child = {} # char to other TrieNode
    self.is_end = False

class Trie(object):
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root
    for c in word:
      if c not in node.child:
        node.child[c] = TrieNode()
      node = node.child[c]
    node.is_end = True

# Sement-Tree (store ops of an interval, really good problem 307, 308)

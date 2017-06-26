"""
170. Two Sum III - Data structure design (Easy)

Design and implement a TwoSum class. It should support the following operations:add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""

class TwoSum(object):
  def __init__(self):
    self.table = set()

  def add(self, value):
    self.table.add(value)

  def find(self, value):
    for item in self.table:
      if value-item in self.table: return True
    return False


if __name__ == '__main__':
  a = TwoSum()
  a.add(1)
  a.add(3)
  a.add(5)
  print a.find(4)
  print a.find(7)

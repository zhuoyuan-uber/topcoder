'''
35. Search Insert Position (Easy)

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 : 2
[1,3,5,6], 2 : 1
[1,3,5,6], 7 : 4
[1,3,5,6], 0 : 0
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        i = 0
        j = n
        while i < j:
            mid = (i + j) / 2
            if nums[mid] > target:
                j = mid
            elif nums[mid] == target:
                return mid
            else:
                i = mid + 1
        return max(i, j)


if __name__ == "__main__":
    a = Solution()
    print a.searchInsert([1,3,5,6], 5)
    print a.searchInsert([1,3,5,6], 2)
    print a.searchInsert([1,3,5,6], 7)
    print a.searchInsert([1,3,5,6], 0)
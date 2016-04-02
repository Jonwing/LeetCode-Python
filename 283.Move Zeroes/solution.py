#! /user/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
    def moveZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead
        """
        if nums:
            cursor = 0
            for num in nums:
                if num != 0:
                    nums[cursor] = num
                    cursor += 1
            while cursor < len(nums):
                nums[cursor] = 0
                cursor += 1


if __name__ == "__main__":
    import random
    arr = [random.randint(0, 10) for i in range(10)]
    print 'initial array: ', arr
    Solution().moveZeros(arr)
    print 'after moving zeros: ', arr

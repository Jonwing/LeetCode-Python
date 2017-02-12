# coding: utf-8


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                r.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return r

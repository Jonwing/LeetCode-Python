#! /user/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ref = {}
        for i, num in enumerate(nums):
            if num in ref:
                return [ref[num], i]
            else:
                ref[target - num] = i

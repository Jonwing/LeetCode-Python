#! /user/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
    def isAnagram(self, s, t):
        '''
        :type s: str
        :type t: str
        :rtype: bool
        '''
        ds = {}
        dt = {}
        for char in s:
            if char in ds:
                ds[char] += 1
            else:
                ds.update({char: 1})

        for char in t:
            if char in dt:
                dt[char] += 1
            else:
                dt.update({char: 1})

        return ds == dt

    def is_anagram_one_dict(self, s, t):
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count.update({char: 1})
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                count.update({char: 1})
        for char in count:
            if count[char] != 0:
                return False
        return True

if __name__ == '__main__':
    s = 'ba'
    t = 'abc'
    print Solution().is_anagram_one_dict(s, t)

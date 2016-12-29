# coding: utf-8


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = {}
        for char in s + t:
            letters[char] = letters.get(char, 0) + 1
        for k, v in letters.items():
            if v % 2 == 1:
                return v

    def findTheDifference2(self, s, t):
        result = 0
        for char in s + t:
            result ^= ord(char)
        # use unichr if necessary
        return chr(result)

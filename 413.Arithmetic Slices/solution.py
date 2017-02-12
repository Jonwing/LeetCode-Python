# coding: utf-8


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = current = 0
        i = 2
        while i < len(A):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                current += 1
                count += current
            else:
                current = 0
            i += 1
        return count

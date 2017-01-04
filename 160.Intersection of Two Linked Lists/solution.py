#! /user/bin/env python
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    '''
    两个链表从头开始遍历，任何一个链表到尾还没找出交叉点时，将其指针置于另一个链表的
    头部继续遍历，这样如果有交叉点，从headA 和 headB 到交叉点的距离是一样的。
    '''
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        if not (a and b):
            return None
        while a is not None and b is not None and a != b:
            a = a.next
            b = b.next

            if a == b:
                return a

            if a is None:
                a = headB
            if b is None:
                b = headA
        return a

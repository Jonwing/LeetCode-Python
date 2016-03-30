#! /user/bin/env python
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        if root:
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
        return root

    def invert_tree_non_recursive(self, root):
        uninverted = [root]
        while uninverted:
            node = uninverted.pop()
            if node:
                node.left, node.right = node.right, node.left
                uninverted.extend([node.left, node.right])
        return root

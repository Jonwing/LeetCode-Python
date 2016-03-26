#! /user/bin/env python
# -*- coding:utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def max_depth_non_recursive(self, root):
        if not root:
            return 0
        visited_nodes = []
        node = root
        max_depth = node.depth = 1
        node.visited = True
        visited_nodes.append(node)
        while (node.left or node.right or visited_nodes):
            if node.left and not hasattr(node.left, 'visited'):
                node.left.depth = node.depth + 1
                node = node.left
                max_depth = max(max_depth, node.depth)
                node.visited = True
                visited_nodes.append(node)
            elif node.right and not hasattr(node.right, 'visited'):
                node.right.depth = node.depth + 1
                node = node.right
                max_depth = max(max_depth, node.depth)
                node.visited = True
                visited_nodes.append(node)
            elif visited_nodes:
                node = visited_nodes.pop()
            else:
                break
        return max_depth


if __name__ == '__main__':
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    root.left = n2
    root.right = n3
    n3.left = n4
    n3.right = n5

    solution = Solution()
    print "recursive solution: ", solution.maxDepth(root)
    print "non-recursive solution: ", solution.max_depth_non_recursive(root)

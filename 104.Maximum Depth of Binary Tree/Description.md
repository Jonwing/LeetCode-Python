Maximum Depth of Binary Tree
===

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

---

递归方式很简单，也容易懂。但是非递归怎么做呢？

用一个list保存已经访问过的节点，从根节点开始遍历，每遍历一个子节点，该节点的深度就+1。没有子节点时回溯到上一个节点，寻找没有访问过的节点重新开始遍历，从而得出最大深度。

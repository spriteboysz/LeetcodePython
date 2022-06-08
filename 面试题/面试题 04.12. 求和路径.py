#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-08 22:12
LastEditTime: 2022-06-08 22:12
Description:
FilePath: 面试题 04.12. 求和路径.py
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def path(node, sum):
            if not node:
                return 0
            count = 0
            if node.val == sum:
                count += 1
            count += path(node.left, sum - node.val)
            count += path(node.right, sum - node.val)
            return count

        if not root:
            return 0
        return path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-10 22:20
LastEditTime: 2022-06-10 22:20
Description:
FilePath: 剑指 Offer II 050. 向下的路径节点之和.py
"""


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def path(node, targetSum):
            if not node:
                return 0
            count = 0
            if node.val == targetSum:
                count += 1
            count += path(node.left, targetSum - node.val)
            count += path(node.right, targetSum - node.val)
            return count

        if not root:
            return 0
        count = path(root, targetSum)
        count += self.pathSum(root.left, targetSum)
        count += self.pathSum(root.right, targetSum)
        return count

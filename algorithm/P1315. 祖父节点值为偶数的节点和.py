#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-03 22:09:27
LastEditTime: 2022-04-03 22:12:29
Description: 
FilePath: 1315.祖父节点值为偶数的节点和.py
"""
#
# @lc app=leetcode.cn id=1315 lang=python3
#
# [1315] 祖父节点值为偶数的节点和
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum_ = 0

        def grandparent(node, n):
            nonlocal sum_
            if not node:
                return
            if n == 2:
                sum_ += node.val
            else:
                grandparent(node.left, n + 1)
                grandparent(node.right, n + 1)

        def dfs(node):
            if not node:
                return
            if node.val % 2 == 0:
                grandparent(node, 0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return sum_


# @lc code=end

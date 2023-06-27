#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-09 22:55:56
LastEditTime: 2022-04-09 23:03:08
Description:
FilePath: 1026.节点与其祖先之间的最大差值.py
"""
#
# @lc app=leetcode.cn id=1026 lang=python3
#
# [1026] 节点与其祖先之间的最大差值
#

# @lc code=start
from typing import Optional


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node, maximum, minimum):
            nonlocal maxvalue
            if not node:
                maxvalue = max(maximum - minimum, maxvalue)
            else:
                maximum, minimum = max(maximum, node.val), min(minimum, node.val)
                dfs(node.left, maximum, minimum)
                dfs(node.right, maximum, minimum)

        maxvalue = 0
        dfs(root, 0, 100001)
        return maxvalue

# @lc code=end

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-10 13:53:20
LastEditTime: 2022-04-10 13:56:21
Description: 
FilePath: 337.打家劫舍-iii.py
"""


#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left = dfs(node.left)
            right = dfs(node.right)
            value1 = node.val + left[1] + right[1]
            value2 = max(left) + max(right)
            return value1, value2

        return max(dfs(root))

# @lc code=end

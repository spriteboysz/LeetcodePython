#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-30 23:15:21
LastEditTime: 2022-03-30 23:17:18
Description: 
FilePath: 98.验证二叉搜索树.py
"""


#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.values.append(node.val)
            dfs(node.right)

        self.values = []
        dfs(root)
        # print(self.values)
        for i in range(len(self.values) - 1):
            if self.values[i] >= self.values[i + 1]:
                return False
        return True

# @lc code=end

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-08 23:45:28
LastEditTime: 2022-03-08 23:49:44
Description: 
FilePath: 938.二叉搜索树的范围和.py
"""


#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        value = []

        def dfs(node):
            if not node:
                return 0
            if low <= node.val <= high:
                value.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return sum(value)

# @lc code=end

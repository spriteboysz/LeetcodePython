#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-08 23:14:00
LastEditTime: 2022-03-08 23:24:58
Description: 
FilePath: 783.二叉搜索树节点最小距离.py
"""
#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        value = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            value.append(node.val)
            dfs(node.right)

        dfs(root)
        return min(value[i + 1] - value[i] for i in range(len(value) - 1))


# @lc code=end

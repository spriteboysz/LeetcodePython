#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-28 23:34:44
LastEditTime: 2022-03-28 23:40:06
Description: 
FilePath: 530.二叉搜索树的最小绝对差.py
"""
#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
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
    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.values.append(node.val)
            dfs(node.right)

        self.values = []
        dfs(root)
        print(self.values)

        minimum = inf
        for i in range(1, len(self.values)):
            minimum = min(self.values[i] - self.values[i - 1], minimum)
        return minimum


# @lc code=end

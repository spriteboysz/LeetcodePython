#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-27 22:36:05
LastEditTime: 2022-03-27 22:38:55
Description: 
FilePath: 671.二叉树中第二小的节点.py
"""
#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return
            self.values.add(node.val)
            dfs(node.left)
            dfs(node.right)

        self.values = set()
        dfs(root)
        if len(self.values) == 1:
            return -1
        else:
            return sorted(list(self.values))[1]


# @lc code=end

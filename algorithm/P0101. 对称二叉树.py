#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-07 23:12:07
LastEditTime: 2022-03-07 23:14:18
Description: 
FilePath: 101.对称二叉树.py
"""


#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            else:
                return dfs(p.left, q.right) and dfs(p.right, q.left)

        return dfs(root.left, root.right)

# @lc code=end

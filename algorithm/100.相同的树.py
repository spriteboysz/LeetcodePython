#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-07 22:54:59
LastEditTime: 2022-03-07 22:55:20
Description: 
FilePath: 100.相同的树.py
"""
#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        # if p is None and q is not None:
        #     return False
        # if p is not None and q is None:
        #     return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# @lc code=end

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-07 23:41:03
LastEditTime: 2022-03-07 23:45:24
Description: 
FilePath: 501.二叉搜索树中的众数.py
"""
#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        value = []
        if not root:
            pass


# @lc code=end

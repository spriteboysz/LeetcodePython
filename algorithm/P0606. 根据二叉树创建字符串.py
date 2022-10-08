#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-08 00:03:50
LastEditTime: 2022-03-08 00:04:26
Description: 
FilePath: 606.根据二叉树创建字符串.py
"""
#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        s = str(root.val)
        if not root.left and not root.right:
            return s

        lv = self.tree2str(root.left)
        rv = self.tree2str(root.right)
        s += "(" + lv + ")"
        if rv:
            s += "(" + rv + ")"
        return s


# @lc code=end

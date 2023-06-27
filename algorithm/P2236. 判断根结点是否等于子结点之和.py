#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-20 22:00:34
LastEditTime: 2022-04-20 22:01:50
Description: 
FilePath: 2236.判断根结点是否等于子结点之和.py
"""
#
# @lc app=leetcode.cn id=2236 lang=python3
#
# [2236] 判断根结点是否等于子结点之和
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
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val

# @lc code=end

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-17 00:06:13
LastEditTime: 2022-02-17 00:08:10
Description: 
FilePath: 144.二叉树的前序遍历.py
"""
#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return (
                [root.val]
                + self.preorderTraversal(root.left)
                + self.preorderTraversal(root.right)
            )


# @lc code=end

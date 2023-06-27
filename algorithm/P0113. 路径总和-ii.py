#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-22 23:06:20
LastEditTime: 2022-03-22 23:07:01
Description: 
FilePath: 113.路径总和-ii.py
"""
#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, targetSum, res, path):
            if not node:
                return
            if not node.left and not node.right:
                if targetSum == node.val:
                    res.append(path + [node.val])
            dfs(node.left, targetSum - node.val, res, path + [node.val])
            dfs(node.right, targetSum - node.val, res, path + [node.val])

        res = []
        dfs(root, targetSum, res, [])
        return res

# @lc code=end

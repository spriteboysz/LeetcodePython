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

from collections import defaultdict
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
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.valuecount[node.val] += 1
            dfs(node.right)

        self.valuecount = defaultdict(int)
        dfs(root)
        maxvalue = []
        _, maxcount = max(self.valuecount.items(), key=lambda el: el[1])
        for k, v in filter(lambda el: el[1] == maxcount, self.valuecount.items()):
            maxvalue.append(k)
        return maxvalue


# @lc code=end

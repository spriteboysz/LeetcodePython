#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 21:29:11
LastEditTime: 2022-04-05 21:31:06
Description: 
FilePath: 508.出现次数最多的子树元素和.py
"""
#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
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
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        treesum = []

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            treesum.append(left + right + node.val)
            return treesum[-1]

        dfs(root)
        print(treesum)
        sumcount = defaultdict(int)
        for item in treesum:
            sumcount[item] += 1
        maximumcount = max(sumcount.values())
        return [key for key, value in sumcount.items() if value == maximumcount]

# @lc code=end

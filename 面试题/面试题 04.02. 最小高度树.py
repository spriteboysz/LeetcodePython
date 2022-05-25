#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-24 22:58
LastEditTime: 2022-05-24 22:58
Description:
FilePath: 面试题 04.02. 最小高度树.py
"""

from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return

        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node

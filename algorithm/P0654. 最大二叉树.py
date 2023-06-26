#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 22:24:35
LastEditTime: 2022-04-05 22:40:21
Description: 
FilePath: 654.最大二叉树.py
"""
#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
from typing import List

from common.TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def create(nums):
            if not nums:
                return
            value = max(nums)
            index = nums.index(value)
            node = TreeNode(value)
            node.left = create(nums[:index])
            node.right = create(nums[index + 1:])
            return node

        root = create(nums)
        return root

# @lc code=end

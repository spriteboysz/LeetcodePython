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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def maketree(nums):
            if not nums:
                return
            value = max(nums)
            index = nums.index(value)
            node = TreeNode(value)
            node.left = maketree(nums[:index])
            node.right = maketree(nums[index + 1 :])
            return node

        root = maketree(nums)
        return root


# @lc code=end

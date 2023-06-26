#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-06 22:12:20
LastEditTime: 2022-04-06 22:13:36
Description: 
FilePath: 108.将有序数组转换为二叉搜索树.py
"""
#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
from typing import Optional, List

from common.TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create(nums):
            if not nums:
                return
            index = (len(nums) - 1) // 2
            node = TreeNode(nums[index])
            node.left = create(nums[:index])
            node.right = create(nums[index + 1 :])
            return node

        root = create(nums)
        print(type(root))
        return root


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    root = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(root)

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        print(node.val)
        dfs(node.right)

    dfs(root)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-25 00:01
FileName: algorithm/P2415. 反转二叉树的奇数层.py
Description: 
"""
from typing import Optional
from common.TreeNode import TreeNode


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return root


if __name__ == '__main__':
    root = TreeNode.create("[7,13,11]")
    solution = Solution().reverseOddLevels(root)
    print(solution)

#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-08 21:57
FileName: algorithm
Description:P0979. 在二叉树中分配硬币.py 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal count
            count += abs(left) + abs(right)
            return left + right + root.val - 1

        count = 0
        dfs(root)
        return count


if __name__ == '__main__':
    root = TreeNode.create("[3,0,0]")
    print(Solution().distributeCoins(root))

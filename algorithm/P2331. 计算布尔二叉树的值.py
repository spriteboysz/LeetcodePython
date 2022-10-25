#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-25 23:35
FileName: algorithm/P2331. 计算布尔二叉树的值.py
Description: 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        elif root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        else:
            return bool(root.val)


if __name__ == '__main__':
    tree = TreeNode.create("[2,1,3,null,null,0,1]")
    solution = Solution().evaluateTree(tree)
    print(solution)

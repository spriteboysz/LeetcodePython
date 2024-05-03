#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-03 14:12
FileName: LCP
Description:P0669. 修剪二叉搜索树.py 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


if __name__ == '__main__':
    root = TreeNode().create('[3,0,4,null,2,null,null,1]')
    print(Solution().trimBST(root, low=1, high=3))

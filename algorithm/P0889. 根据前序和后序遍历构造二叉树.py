#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-03 11:32
FileName: algorithm
Description:P0889. 根据前序和后序遍历构造二叉树.py 
"""
from typing import List, Optional

from common.TreeNode import TreeNode


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        index = postorder.index(preorder[1]) + 1
        root.left = self.constructFromPrePost(preorder[1:index + 1], postorder[:index])
        root.right = self.constructFromPrePost(preorder[index + 1:], postorder[index:-1])
        return root


if __name__ == '__main__':
    print(Solution().constructFromPrePost(preorder=[1, 2, 4, 5, 3, 6, 7], postorder=[4, 5, 2, 6, 7, 3, 1]))

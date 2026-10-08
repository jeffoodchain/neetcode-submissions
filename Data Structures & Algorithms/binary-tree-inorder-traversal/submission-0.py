# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left > root > right
        def inorder(root: Optional[TreeNode], vec: List[int]) -> List[int]:
            if root:
                inorder(root.left, vec)
                vec.append(root.val)
                inorder(root.right, vec)
            return vec
        vec = []
        return inorder(root, vec)
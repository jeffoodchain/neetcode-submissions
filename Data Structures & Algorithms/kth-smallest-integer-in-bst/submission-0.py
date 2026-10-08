# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def treeToList(root: Optional[TreeNode], vec: List[int]) -> List[int]:
            if root:
                treeToList(root.left, vec)
                vec.append(root.val)
                treeToList(root.right, vec)
        vec = []
        treeToList(root, vec)
        return vec[k-1]
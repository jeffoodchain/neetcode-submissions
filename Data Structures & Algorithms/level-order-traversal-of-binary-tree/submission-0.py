# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        
        results = []

        if root:
            q.append(root)
        
        while q:
            sublist = []
            for i in range(len(q)):
                popped = q.popleft()
                sublist.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            results.append(sublist)
        return results

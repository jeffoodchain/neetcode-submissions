class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not self.root:
            self.root = newNode
            return
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = newNode
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = newNode
                    return
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
    
        while True:
            if not curr:
                return -1
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        
    def getMin(self) -> int:
        curr = self.root

        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root

        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if not curr:
            return

        if key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        elif key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr


    def getInorderKeys(self) -> List[int]:
        res = []
        self.inorderTraversal(self.root, res)
        return res

    def inorderTraversal(self, root: TreeNode, vec: List[int]) -> None:
        # Left > Root > Right
        if root:
            self.inorderTraversal(root.left, vec)
            vec.append(root.key)
            self.inorderTraversal(root.right, vec)

    def findMin(self, root: TreeNode) -> TreeNode:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
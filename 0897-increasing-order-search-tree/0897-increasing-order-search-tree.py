class Solution:
    def increasingBST(self, root):
        self.ans = TreeNode(0)
        self.head = self.ans

        self.incOrder(root)

        return self.head.right

    def incOrder(self, root):
        if root is None:
            return

        self.incOrder(root.left)

        self.ans.right = root
        root.left = None
        self.ans = self.ans.right

        self.incOrder(root.right)

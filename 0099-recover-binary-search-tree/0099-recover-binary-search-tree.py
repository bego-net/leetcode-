class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val
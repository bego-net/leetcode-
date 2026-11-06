class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # Base case
        if not inorder:
            return None
        
        # The last element of postorder list is the root
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # Find the position of the root in the inorder list
        inorder_index = inorder.index(root_val)
        
        # Recursively build the left and right subtrees
        root.right = self.buildTree(inorder[inorder_index+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        
        return root
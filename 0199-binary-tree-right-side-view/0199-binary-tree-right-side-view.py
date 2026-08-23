class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = [root]
        curr = 0
        ans = []
        
        while curr < len(queue):
            ans.append(queue[curr].val)
            qSize = len(queue)
            
            for i in range(curr, qSize):
                if queue[i].right:
                    queue.append(queue[i].right)
                if queue[i].left:
                    queue.append(queue[i].left)
            
            curr = qSize
        
        return ans
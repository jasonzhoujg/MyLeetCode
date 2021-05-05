class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        stack_next = [root]
        res_sum = []
        stack = []
        level=[]
        while stack_next :
            stack = [i for i in stack_next]
            stack_next = []
            level=[]
            for cur in stack:
                level.append(cur.val)
                if cur.left:stack_next.append(cur.left)
                if cur.right:stack_next.append(cur.right)

            res_sum.append(level)
            

        return res_sum

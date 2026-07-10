class Solution:   
    def isSubtree(self, root, subRoot):


        def sameTree(p, q):

            if not p and not q:
                return True


            if not p or not q:
                return False


            if p.val != q.val:
                return False


            left = sameTree(p.left, q.left)
            right = sameTree(p.right, q.right)


            return left and right



        def subTree(root):

            if not root:
                return False


            if sameTree(root, subRoot):
                return True


            left = subTree(root.left)
            right = subTree(root.right)


            return left or right



        return subTree(root)
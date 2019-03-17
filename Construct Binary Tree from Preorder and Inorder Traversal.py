import sys

#利用前序和中序遍历确定一棵树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):

        return self.tree(inorder, preorder)

    def tree(self, inorder, preorder):#利用前序和中序遍历确定一棵树
        if len(inorder) > 0:
            root = TreeNode(preorder[0])
            ind = inorder.index(root.val)
            inorderleft = inorder[0:ind]
            # if ind+1<len(inorder)-1:
            inorderright = inorder[ind + 1:len(inorder)]
            preorderleft = preorder[1:ind + 1]
            preorderright = preorder[ind + 1:len(inorder)]
            root.left = self.tree(inorderleft, preorderleft)
            root.right = self.tree(inorderright, preorderright)
            # else:
            #     root =None
        else:
            root = None

        return root

    def preOrder(self,root,tree):#树的前序遍历
        if(root!=None):
            tree.append(root.val)
        if(root.left!=None):
            self. preOrder(root.left,tree)
        if(root.right != None):
            self. preOrder(root.right,tree)
        return tree

if __name__ == "__main__":
    # height = sys.stdin.readline().strip()
    # height = height.split(" ")
    # height = [int(x) for x in height]
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]#input为preorder和inorder


    NewSolution=Solution()
    tree=[]
    root=NewSolution.buildTree(preorder, inorder)
    print(NewSolution.traversalTree(root,tree))

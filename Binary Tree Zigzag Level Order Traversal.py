#之字型层次遍历树
#input：层次遍历[3,9,20,null,null,15,7]
#outPut：
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

#需要两个栈
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #之字型遍历
    def zigzagLevelOrder(self, root: TreeNode) :

        stack1 = []
        stack2 = []
        inorder = []

        stack1.append(root)

        while root != None or stack1 != [] or stack2 != []:
            suborder = []
            while stack1 != []:
                root = stack1.pop()
                if root != None:
                    suborder.append(root.val)
                    stack2.append(root.left)
                    stack2.append(root.right)
                if stack1 == [] and suborder != []:
                    inorder.append(suborder)
                    suborder = []
            while stack2 != []:
                root = stack2.pop()
                if root != None:
                    suborder.append(root.val)
                    stack1.append(root.right)
                    stack1.append(root.left)
                if stack2 == [] and suborder != []:
                    inorder.append(suborder)
                    suborder = []

        return inorder

    # 根据层次遍历建一颗树,有None才可以依据level_order构造一棵树
    def builtTreeByLevelOrder(self, level_order):
        treeNodeList=[TreeNode(node) for node in level_order]
        i=0
        while i<len(treeNodeList):
            if(treeNodeList[i]!=None):
                if(2*i+1<len(treeNodeList)):
                    treeNodeList[i].left=treeNodeList[2*i+1]
                else:
                    treeNodeList[i].left =None
                if (2 * i + 2 < len(treeNodeList)):
                    treeNodeList[i].right = treeNodeList[2 * i + 2]
                else:
                    treeNodeList[i].right =None
                i=i+1
        return treeNodeList[0]

    # 树的前序遍历
    def preOrderTree(self,root,tree):
        if(root!=None):
            tree.append(root.val)
        if(root.left!=None):
            self.preOrderTree(root.left,tree)
        if(root.right != None):
            self.preOrderTree(root.right,tree)
        return tree
    
if __name__ == "__main__":
    level_order=[3,9,20,None,None,15,7]
    newsolution=Solution()
    root=newsolution.builtTreeByLevelOrder(level_order)#先构造一棵树
    tree=[]
    preOrder=newsolution.preOrderTree(root,tree) #前序遍历该树

    levelOrder=newsolution. zigzagLevelOrder(root)#层次遍历一棵树

    print(levelOrder)
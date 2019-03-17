#非递归的中序遍历,stack

#inputInput: [1,null,2,3]
#Output: [1,3,2]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #中序遍历
    def inorderTraversal(self, root: TreeNode) :
        inorder = []
        stack = []

        while (root != None or stack != []):
            if (root != None):
                if(root.val!=None):
                    stack.append(root)
                root = root.left
            else:
                root = stack.pop();
                if (root.val != None):
                    inorder.append(root.val)
                root = root.right

        return inorder

    # 根据层次遍历建一颗树,有None才可以依据level_order构造一棵树
    def builtTreeByLevelOrder(self, level_order):
        treeNodeList=[TreeNode(node) for node in level_order]
        i=0
        while i<len(treeNodeList):
            if(treeNodeList[i]!=None):
                if(2*i+1<len(treeNodeList)):
                    treeNodeList[i].left=treeNodeList[2*i+1]
                if (2 * i + 2 < len(treeNodeList)):
                    treeNodeList[i].right = treeNodeList[2 * i + 2]
                i=i+1
        return treeNodeList[0]

if __name__ == "__main__":
    level_order=[3,9,20,None,None,15,7]
    newsolution=Solution()
    root=newsolution.builtTreeByLevelOrder(level_order)#先构造一棵树
    print(root)

    inOrder=newsolution.inorderTraversal(root)#层次遍历一棵树

    print(inOrder)
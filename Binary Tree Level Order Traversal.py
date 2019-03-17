#二叉树层次遍历

#input：层次遍历
#[3,9,20,null,null,15,7]

#output：
# [[3],
#   [9,20],
#   [15,7]]

#使用队列实现，读取第一个root的值，并将root的左右root添加至队列，原root出队

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #树的层次遍历
    def levelOrder(self, root: TreeNode):
        queue = []
        order = []
        i = 0
        root = [root, 0]
        while root[0] != None or queue != []:
            if (root[0] != None):
                order.append([])
                order[root[1]].append(root[0].val)
                i = root[1] + 1
                queue.append([root[0].left, i])
                queue.append([root[0].right, i])
            if queue != []:
                root = queue.pop(0)
        inorder = []
        for i in order:
            if i != []:
                inorder.append(i)
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

    levelOrder=newsolution.levelOrder(root)#层次遍历一棵树

    print(levelOrder)


# 作者: Antenna
# 2026年05月29日22时19分13秒
# Antenna2000@163.com
class Node:
    """
    节点类
    """
    def __init__(self,element = -1,lchild=None,rchild=None):
        self.element = element
        self.lchild = lchild
        self.rchild = rchild

class Tree:
    """
    树类
    """
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self,element):
        """
        为树添加节点，层次建树
        :param element: 新节点的值
        :return: None
        """
        node = Node(element)
        if self.root.element == -1: #如果树是空的，对根节点赋值
            self.root = node
            self.myQueue.append(self.root) #根节点入队
        else:
            treeNode:Node = self.myQueue[0] #此节点的子树还没齐
            if treeNode.lchild is None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild) #新节点入队
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild) #新节点入队
                self.myQueue.pop(0)  #此节点以存在右子树，将其出队

    def pre_order(self,root):
        """
        先序遍历
        :param root: 根节点
        :return: None
        """
        if root:
            print(root.element,end=" ")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self,root):
        """
        中序遍历
        :param root: 根节点
        :return: None
        """
        if root:
            self.in_order(root.lchild)
            print(root.element,end=" ")
            self.in_order(root.rchild)

    def post_order(self,root):
        """
        后序遍历
        :param root: 根节点
        :return: None
        """
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.element,end=" ")

    def level_order(self,root):
        """
        利用辅助队列层序遍历
        :param root: 根节点
        :return: None
        """
        if root:
            myQueue = []
            node = root
            myQueue.append(node)
            while myQueue:
                node = myQueue.pop(0)
                print(node.element,end=" ")
                if node.lchild:
                    myQueue.append(node.lchild)
                if node.rchild:
                    myQueue.append(node.rchild)

if __name__ == '__main__':
    """主函数"""
    tree = Tree() #新建一个树对象
    for element in range(10):
        tree.add(element)

    print("层次遍历：")
    tree.level_order(tree.root)
    print("\n先序遍历:")
    tree.pre_order(tree.root)
    print("\n中序遍历:")
    tree.in_order(tree.root)
    print("\n后序遍历:")
    tree.post_order(tree.root)
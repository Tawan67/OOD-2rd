class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = None if left == None else left
        self.right = None if right == None else right
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self,root = None):
        self.root = None if root == None else root
        
    def insert(self, data):
        if self.root == None:
            self.root = BST._add(self.root, data)
            return self.root
        return BST._add(self.root,data)
        
    def _add(root,data):
        if root == None:
            return Node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left,data)
            else:
                root.right = BST._add(root.right,data)
               
        return root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def rebalance(self):
        return BST.balance_re(self.root)

    def balance_re():
        pass
            
            
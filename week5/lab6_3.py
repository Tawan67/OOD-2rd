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
            elif data > root.data:
                root.right = BST._add(root.right,data)
            
        return root
    def printTreeB(self):
        self.printTree(self.root)
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def find_me(self,result):
        return BST.path_sum(self.root,result)

    
    def inOrder(self):
        return BST._inO(self.root)
        
        
    def _inO(root = None,li = None):
        if li == None:
            li = []
        if root != None:
            BST._inO(root.left,li)
            li.append(root.data)
            BST._inO(root.right,li)
            return li
        else :
            return
    
    def check_multi(self,k):
        return BST.check_multi1(k,self.root)
    def check_multi1(k,root):
        if root != None:
            if root.data > k:
                root.data = root.data*k
            BST.check_multi1(k,root.left)
            BST.check_multi1(k,root.right)
            return 
        else :
            return
        
def sum_li(li:list):
    if len(li)<1:
        return
    n = 0
    for i in li:
        n+=i
    return n  
        
def main():
    print("**Sum of tree**")
    inp = input("Enter input : ")
    inp,k = inp.split("/")
    k = int(k)
    inp = [int(i) for i in inp.split(" ")]
    # print(inp)
    # print(k)
    T = BST()
    for i in inp:
        root = T.insert(i)
    print("\nTree before:")
    T.printTree(root)
    sum = T.inOrder()
    sum = sum_li(sum)
    print(f"Sum of all nodes = {sum}")
    print()
    print("Tree after:")
    T.check_multi(k)
    T.printTreeB()
    sum = T.inOrder()
    sum = sum_li(sum)
    print(f"Sum of all nodes = {sum}")
main()  
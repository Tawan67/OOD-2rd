class AVLTree:

    class AVLNode:

        def __init__(self, data, left = None, right = None):

            self.data = data

            self.left = None if left is None else left

            self.right = None if right is None else right

            self.height = self.setHeight()

        

        def __str__(self):

            return str(self.data)

        

        def setHeight(self):

                a = self.getHeight(self.left)

                b = self.getHeight(self.right)

                self.height = 1 + max(a,b)

                return self.height

            

        def getHeight(self, node):

            return -1 if node == None else node.height

            

        def balanceValue(self):      

            return self.getHeight(self.right) - self.getHeight(self.left)

    

    def __init__(self, root = None):

        self.root = None if root is None else root

    
    def rebalance(data,root):
        if root == None:
            return
        # root.left = AVLTree.rebalance(data,root.left)
        # root.right = AVLTree.rebalance(data,root.right)
        if root.balanceValue() > 1 or root.balanceValue() < -1:
            # print("aaaaaa")
            balance = root.balanceValue()
            #LL LR
            if balance < -1:
                
                if data < root.left.data:
                    return AVLTree.rotateRightChild(root)
                elif root.left != None:
                    root.left = AVLTree.rotateLeftChild(root)
                    return AVLTree.rotateRightChild(root)
            #RR RL
            if balance > 1:
                if data > root.right.data:
                    return AVLTree.rotateLeftChild(root)
                elif root.right != None:
                    root.right = AVLTree.rotateRightChild(root.right)
                    return AVLTree.rotateLeftChild(root)
            
        # print("inre")
        return root
                
                
            
    def add(self, data):
        try:
            data = int(data)
        except:
            pass
        if self.root == None:
            self.root = AVLTree.AVLNode(data)
            return 0
        else:
            self.root = AVLTree._add(self.root,data)
        # if self.root.balanceValue() > 1 or self.root.balanceValue() < -1:
        #     self.root = AVLTree.rebalance(data,self.root)
        return self.root
        # code here

 

    def _add(root,data):
        if root == None:
            return AVLTree.AVLNode(data)
        
        if data < root.data:
            root.left = AVLTree._add(root.left,data)
        elif data >= root.data:
            root.right = AVLTree._add(root.right,data)
        if root != None:
            root.setHeight() 
        if root.balanceValue() > 1 or root.balanceValue() < -1:
                # AVLTree.rebalance(data,root)
            balance = root.balanceValue()
            #LL LR
            if balance < -1:
                # AVLTree._printTree(root)
                if data < root.left.data:
                    return AVLTree.rotateRightChild(root)
                elif root.left != None and data >= root.left.data:
                    root.left = AVLTree.rotateLeftChild(root.left)
                    return AVLTree.rotateRightChild(root)
            #RR RL
            if balance > 1:
                if data >= root.right.data:
                    return AVLTree.rotateLeftChild(root)
                elif root.right != None and data < root.right.data:
                    # AVLTree._printTree(root)
                    # print(root)
                    root.right = AVLTree.rotateRightChild(root.right)
                    return AVLTree.rotateLeftChild(root)
    
   
            
                
        return root
        

        # code here



    def rotateLeftChild(z) : # base is balance ==1 or == 0 return to rotateLeft
        if z.right == None:
            return z
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.setHeight()
        y.setHeight()
        return y
         # code here



    def rotateRightChild(z):
        if z.left == None:
            return z
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.setHeight()
        y.setHeight()
        return y

          # code here  



    def postOrder(self):
        print("AVLTree post-order : ",end="")
        AVLTree._postOrder(self.root)
        print()
        
         # code here



    def _postOrder(root):
        if root != None:
            AVLTree._postOrder(root.left)
            AVLTree._postOrder(root.right)
            print(root.data,end =" ")
         # code here



    def printTree(self):
        
        AVLTree._printTree(self.root)

        print()

    

    def _printTree(node , level=0):
        if node is not None:
            if node.data == None:
                return
            AVLTree._printTree(node.right, level + 1)

            print('    ' * level + str(node.data))
            AVLTree._printTree(node.left, level + 1)
        
    def delNode(node,target):
        if node.left == target:
            result = node.left
            node.left = None
            return result
        elif node.right == target:
            result = node.right
            node.right = None
            return result
    def compareTree(self,anotherTree):
        return AVLTree._compareTree(self.root,anotherTree.root)
    def _compareTree(root1,root2):
        if root1 == None or root2 == None:
            return root2 == root1
        if root1.data != root2.data:
                return 0
        if AVLTree._compareTree(root1.left,root2.left) == 0:
            return 0
        if AVLTree._compareTree(root1.right,root2.right) == 0:
            return 0
        return 1
        
            
 
avl1 = AVLTree()
avl2 = AVLTree()
inp = input("Enter Tree1/Tree2 : ").split("/")

for i in inp[0].split(" "):
    try:
        root1 = avl1.add(int(i))
    except:
        root1 = avl1.add(None)
for i in inp[-1].split(" "):
    try:
        root2 = avl2.add(int(i))
    except:
        root2 = avl2.add(None)
print("Tree 1")
avl1.printTree()
print("Tree 2")
avl2.printTree()
same = avl1.compareTree(avl2)
if same:
    print("Same Tree")
else:
    print("Different Tree")

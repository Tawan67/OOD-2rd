class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.h = 1
            
        def update_height(self):
            return BST.Node._update_height(self)
            pass
        def _update_height(root):
            if root == None:
                return 0

            l = BST.Node._update_height(root.left)
            r = BST.Node._update_height(root.right)
            if l > r:
                root.h = l
                return l+1
            else:
                root.h = r
                return l+1
       
        def get_Height(self,node):
            return -1 if node == None else node.h
        def set_Height(self):
            a = self.get_Height(self.left)

            b = self.get_Height(self.right)

            self.height = 1 + max(a,b)

            return self.height
        def balance_factor(self,node):
            return self.get_Height(node.left) - self.get_Height(node.right)
        
    def __init__(self):
        self.root = None
    
    def insert(self,key):
        if not self.root:
            self.root = BST.Node(key)
        else:
            BST._insert(self.root,key)

    def _insert(node,key):
        if key < node.data:
            if node.left:
                BST._insert(node.left,key)
            else:
                node.left = BST.Node(key)
        else:
            if node.right:
                BST._insert(node.right,key)
            else:
                node.right = BST.Node(key)
   

    def _get_format(root,ans = ""):
        if root:
            temp = ""
            if root.right:
                temp += BST._get_format(root.right,ans + "     ")
            temp += f"{ans}{root.data}\n"
            if root.left:
                temp += BST._get_format(root.left,ans + "     ")
            return temp
        return ""
    
    def __str__(self):
        return BST._get_format(self.root)

################################
'''
⠀⠀⢘⣾⣾⣿⣾⣽⣯⣼⣿⣿⣴⣽⣿⣽⣭⣿⣿⣿⣿⣿⣧
⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣰⣯⣾⣿⣿⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
⠀⠀⠛⠛⠋⠁⣠⡼⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠤⣶⣾⣿⣿⣿⣦⡈⠉⠉⠉⠙⠻⣿⣿⣿⣿⣿⠿⠁⠀
⠀⠀⠀⠀⠈⠟⠻⢛⣿⣿⣿⣷⣶⣦⣄⠀⠸⣿⣿⣿⠗⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠀⠄⣿⡿⠋⣉⠈⠙⢿⣿⣦⣿⠏⡠⠂⠀⠀⠀
⠀⠀⠀⠀⢰⡌⠀⢠⠏⠇⢸⡇⠐⠀⡄⣿⣿⣃⠈⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣻⣿⢫⢻⡆⡀⠁⠀⢈⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣻⣷⣾⣿⣿⣷⢾⣽⢭⣍⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⡿⠈⣹⣾⣿⡞⠐⠁⠀⠀⠀⠁⠀⠀⠀
⠀⠀⠀⠨⣟⣿⢟⣯⣶⣿⣆⣘⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡆⠀⠐⠶⠮⡹⣸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

def isAVL(node : BST.Node):
    return not (node.balance_factor(node) > 1 or node.balance_factor(node)<-1)
    
    pass


################################


tree = BST()

print("**********IsAVL**********")
for i in list(map(int, input("Enter numbers to insert in the tree: ").split())):
    tree.insert(i)
tree.root.update_height()
print("Tree:")
print(tree)
print("Is AVL???:", isAVL(tree.root))

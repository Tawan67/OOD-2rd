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
    def search(self,t,e):
        
        return BST._preOrder(self.root,t,e)
    def _preOrder(root:Node,t,e,li = None):
        if li == None:
            li = []
        if root.left != None or root.right != None:
            li.append(root.data)
            if li[-1] == t:
                print("Found Treasure !!!")
            if t in li and li[-1]==e:
                print("Found Escape !!!")
                printli(li,1)
                # print(li)
                print(">>> Mission Complete <<<")
                return 0
            else:
                printli(li)
            # print(li)
            if root.left != None :
                check = BST._preOrder(root.left,t,e,li)
                if check == 0:
                    return 0
            if root.right != None:
                check = BST._preOrder(root.right,t,e,li)
                if check == 0:
                    return 0
            li.pop(-1)
            return li
        if root.left == None and root.right == None:
            li.append(root.data)
            if li[-1] == t:
                print("Found Treasure !!!")
            if t in li and li[-1]==e:
                print("Found Escape !!!")
                printli(li,1)
                # print(li)
                print(">>> Mission Complete <<<")
                return 0
            else:
                printli(li)
                # print(li)
                li.pop(-1)
            return
        
def printli(li:list,true =None):
    if true == None:
        if len(li) == 1:
            print(f"❌ {li[0]}")
        else:
            ans = "❌ "
            for i in range(len(li)-1):
                ans+=f"{li[i]} -> "
            ans+=f"{li[-1]}"
            print(ans)
    else:
        ans = "✅ "
        for i in range(len(li)-1):
            ans+=f"{li[i]} -> "
        ans+=f"{li[-1]}"
        print(ans)
T = BST()
inp,tressure,escape = input("Enter Input : ").split("/")
inp = inp.split(" ")
tressure =int(tressure)
escape = int(escape)
for i in inp:
    root = T.insert(int(i))
T.printTreeB()

print("-------------------------------------------------")
result = T.search(tressure,escape)
if result != 0:
    print(">>> Mission Failed <<<")
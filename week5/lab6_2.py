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
            
    def find_me(self,result):
        return BST.path_sum(self.root,result)

    def path_sum(root,result,li = None):
        if li == None:
            li = []
        # print(f"travel = {root.data}")
        if root.left == None and root.right == None:
            li.append(root.data)
            # print(sum_li(li))
            if root.data == None:
                return False
            if sum_li(li) == result:
                return True
            else:
                li.pop(-1)
                return False
        else:
            li.append(root.data)
        
        if root.left !=None:
            l = BST.path_sum(root.left,result,li)
            if l:
                return l
        if root.right != None:
            r = BST.path_sum(root.right,result,li)
            if not r:
                li.pop(-1)
            return r
        li.pop(-1)
        return False
def sum_li(li:list):
    if len(li)<1:
        return
    n = 0
    for i in li:
        n+=i
    return n        

def main():
    T = BST()
    inp = input("Enter the values to insert into BST and target sum : ").split("/")
    inp_int = [int(i) for i in inp[0].split(" ") if i.isnumeric()]
    result = int(inp[1])
    for i in inp_int:
        root = T.insert(i)
    T.printTree(root)
    print(T.find_me(result))

main()
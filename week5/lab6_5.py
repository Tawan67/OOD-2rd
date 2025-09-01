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
            elif data >= root.data:
                root.right = BST._add(root.right,data)
            
        return root
    def printTreeB(self):
        self.printTree(self.root)
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def command_re(sefl,n,com):
        global change #check that tree has change or not 
        change = 0 #defalt ==  not change
        result = BST._remove(sefl.root,n,com)
        if result:
            change = 1 # if root has to remove (fallen) that mean it's change
            sefl.root = None
        return sefl.root #just return it bor dai chai
    
    
    def _remove(root,n,com,li = None):
        global change
        if li == None:
            li = []
        if root.left != None or root.right != None: # if can go deeper
            li.append(root.data) # preOrder 
            if root.left != None: # in left if it can
                result = BST._remove(root.left,n,com,li) #in left
                if result: #if left is leaf and condition is true
                    change = 1
                    root.left = None #remove leaf
                    
            if root.right != None: #same but right
                result2 = BST._remove(root.right,n,com,li)
                if result2:
                    change = 1
                    root.right = None
                    pass
                    
            if root.left == None and root.right == None: #if left and right were removed we have to check that current node has to remove or not 
                
                # print(li)
                # print("all in")
                if com == 'L':
                    # print("L in")
                    if sum_li(li) < n:
                        printli(li,'L')
                        li.pop(-1)
                        return 1 #return 1 to remove this node
                if com == 'M':
                    if sum_li(li) > n:
                        printli(li,'M')
                        li.pop(-1)
                        return 1
                if com == "EQ":
                    if sum_li(li) ==  n:
                        printli(li,'EQ')
                        li.pop(-1)
                        return 1
                li.pop(-1) # if not remove node you have to pop the element of this node and return to the less deep layer
                return 0
            li.pop(-1) #if this node have way to go but that way is enable to removed node so we have to go to higher node 
            return 0
        
        if root.left == None and root.right == None: #check condition if you are on leaf
            li.append(root.data)
            if com == 'L':
                if sum_li(li) < n:
                    printli(li,'L')
                    li.pop(-1)
                    return 1
            if com == 'M':
                if sum_li(li) > n:
                    printli(li,'M')
                    li.pop(-1)
                    return 1
            if com == "EQ":
                if sum_li(li) ==  n:
                    printli(li,'EQ')
                    li.pop(-1)
                    return 1
            li.pop(-1)
            return 0
change = 0            
def printli(li:list,com):
    global count
    ans = ""
    for i in range(len(li)-1):
        ans+=f"{li[i]}->"
    ans+=f"{li[-1]}"
    print(f"{count[com]}) {ans} = {sum_li(li)}")
    count[com]+=1
                     
                        
def sum_li(li):
    n = 0
    for i in li:
        n+=i
    # print(n)
    return n
    
count = {}
count['L'] = count['M'] = count['EQ'] = 1
 
def main():
    global count
    inp,com = input("Enter <Create City A (BST)>/<Create conditions and deploy the army>: ").split('/')
    inp = [int(i) for i in inp.split(" ")]
    # print(inp)
    try:
        com_dict = []
        com = com.split(",")
        
        for j in com:
            k,v = j.split(" ")
            com_dict.append([k,int(v)])
    except:
        com_dict = {}
        k,v = com.split(" ")
        com_dict[k]=int(v)
    T = BST()
    for i in inp:
        root = T.insert(i)
    print("(City A) Before the war:")
    T.printTreeB()
    for kv in com_dict:
        k = kv[0]
        v = kv[1]
        print("--------------------------------------------------")
        # print(f"{k} = {v}")
        if k == 'L':
            print(f"Removing paths where the sum is less than {v}:")
        elif k == 'M':
            print(f"Removing paths where the sum is greater than {v}:")
        elif k == 'EQ':
            print(f"Removing paths where the sum is equal to {v}:")
        count['L'] = count['M'] = count['EQ'] = 1
        T.command_re(v,k)
        if change == 0:
            print("No paths were removed.")
        print("--------------------------------------------------")
        print("(City A) After the war:")
        if T.root == None:
            print("City A has fallen!")
            return
        else:
            T.printTreeB()
        

main()
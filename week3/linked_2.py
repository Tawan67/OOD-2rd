class LinkedList:
    class Node:
        def __init__(self,data,next = None):
            self.data = data
            if next == None:
                self.next = None
            else:
                self.next = next
        def __str__(self):
            return str(self.data)
            pass
    # def __init__(self):
    #     self.head = None
    #     self.tail = self.head
    #     self.size = 0
    def __init__(self,head = None):
        self.tail= None
        self.size = 0
        if head == None:
            self.head = None
        else:
            self.head = head
            self.size = 1
            t = self.head
            while t.next != None:
                t = t.next
                self.size+=1
    # def append(self,data):
    #     pass


    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node))
            node = node.next
        return '->'.join(ans)

    
    
    
    
    
    # def __str__(self):
    #     if self.isEmpty():
    #         return "Empty"
    #     cur, s = self.head, str(self.head.data) + " "
    #     while cur.next != None:
    #         s += str(cur.next.data) + " "
    #         cur = cur.next
    #     return s
    
    
    def isEmpty(self):
        return self.size ==0
    
    def append(self,data):
        new = self.Node(data)
        if self.head == None:
            self.head = new
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new
        self.size += 1
    
    def addHead(self,data):
        new = self.Node(data)
        if self.head != None:
            new.next = self.head
            self.head = new
        else:
            self.head = new
        self.size+=1
        
    def search(self,data):
        current = self.head
        while current != None:
            if current.data == data:
                return "Found"
            current = current.next
        return "Not Found"
    def size_out(self):
        return self.size
    def index(self,item):
        index = 0
        current = self.head
        while current != None:
            if current.data == item:
                return index
            index+=1
            current =current.next
        return -1
    def pop(self,index):
        if index < 0 or self.head == None:
            return "Out of Range"
        if index == 0:
            item = self.head
            new_head = item.next
            self.head = new_head
            self.size -= 1 
            return item.data
        count = 0
        current = self.head
        while current != None:
            if index == count+1:
               item = current.next
               if item == None:
                   return "Out of Range"
               post = current.next.next
               current.next = post
               self.size -= 1
               return item.data
            current = current.next
            count += 1
        return "Out of Range"    
    def remove_head(self):
        current_head = self.head
        
        if current_head == None:return
        if current_head.next != None:
            new_head = current_head.next
            self.head = new_head
        else:
            self.head = None
        self.size -=1
        return current_head.data

    def remove_tail(self):
        if self.head == None:
            return None
        current = self.head
        if current.next == None:
            self.size -=1
            self.head = None
            return current.data
        else:
            while current.next.next !=None:
                current = current.next
            last = current.next
            current.next = None
            self.size -=1
            return last.data
    
    def insertAfter(self,index,data):
        if index < 0:
            return IndexError
        insert = Node(data)
        current = self.head
        count = 0
        while current != None:
            if count == index:
                insert.next = current.next
                current.next = insert
                self.size += 1
                return
            else:
                current = current.next
                count +=1
        print("can't insert")
        
    def peek(self,index = None,size = None,is_node = None):
        if index == None:
            index = 0
        if size == None:
            size = self.size_out()
        index_cur = 0
        current =self.head
        for i in range(size):
            if index_cur == index:
                if current == None:
                    return None
                if is_node == None:
                    return current.data
                else:
                    return current
            index_cur+=1
            current = current.next
        return None
    def r_shift(self,index):
        if index ==  0:
            target = self.head #0 
            r = target.next # 1
            r_next = target.next.next # 2, 0,1,2
            r.next = target # 1 --> 0
            target.next = r_next # 1-->0-->2
            self.head = r # head -->1-->0-->2
        else:
            check = 0
            for i in range(self.size_out()):
                current = self.head
                if index-1 == check:
                    # print("in2")
                    # be_fore =f"{link}"
                    before = current
                    target = current.next 
                    after = current.next.next # can't be none , switch with target
                    # before,target,after,after_next
                    after_next = after.next
                    after.next = target
                    target.next = after_next
                    before.next = after # before,after,target,after_next
                    # print(f"L = {link} ,before = {be_fore}")
                    return 1,index + 1
                current =current.next
                check+=1
            
            

def find_max(link:LinkedList,size=None):
    if size == None:
        size = link.size_out()
    current  = link.head.data
    index = 0
    for i in range(size):
        if isinstance(link.peek(i,size),str):
            return "Out of Range"
        if link.peek(i,size) >= current:
            current = link.peek(i,size)
            index = i
    return current,index

def find_more_than(link:LinkedList,index):
    if link.peek(index) == None or link.peek(index+1) ==None:
        return 0
    return link.peek(index) > link.peek(index+1)

def swapping(link:LinkedList,index):
    if link.peek(index+1) == None:
        # print("outto+1111")
        return 0,index
    if link.peek(index) > link.peek(index+1):
        check = 0
        current = link.head
        if index == 0:
            # print("in1")
            post = link.peek(0,is_node=1) #head
            pre = post.next #second
            third = post.next.next #third
            pre.next = post #2...1
            post.next = third # 2..1...3 switch 1,2 to 2,1
            link.head = pre # make 2 to head
            return 1,index + 1
        for i in range(link.size_out()):
            if index-1 == check:
                # print("in2")
                be_fore =f"{link}"
                before = current
                target = current.next 
                after = current.next.next # can't be none , switch with target
                # before,target,after,after_next
                after_next = after.next
                after.next = target
                target.next = after_next
                before.next = after # before,after,target,after_next
                # print(f"L = {link} ,before = {be_fore}")
                return 1,index + 1
            current =current.next
            check+=1
    # print("outto",index,link.peek(index),"   ",link.peek(index) > link.peek(index+1))
    return 0,index
def four_of_five(L:LinkedList):
    print(f"Input List: {L}")
    print("_______________________________________")
    for i in range(L.size_out(),0,-1):
        max,index = find_max(L,i)
        # print(f"index = {index}, value = {max}")
        check = 1
        while check:
            check,index=swapping(L,index)
            if check:
                print(f"\nSwapping {L.peek(index)} and {L.peek(index-1)}")
                print(f"List: {L}")
            #     print(index)
            # else:
            #     print(index,L.peek(index),"<",index+1,L.peek(index+1))
    
    print("_______________________________________")
    print(f"Sorted List: {L}")               

def main():
    print("*****Bubble Sort Linked List*****")
    input_1 = input("Enter Input: ").split(",")
    
    L = LinkedList()
    for i in input_1:
        i = int(i)
        L.append(i)
    print(f"Input List: {L}")
    print("_______________________________________")
    # print(L)
    check = 0
    new_val = 1
    index = -1
    s = L.size_out()-1
    while check < L.size_out()-1:
        check = 0
        
        for i in range(L.size_out()-1):
            if not (find_more_than(L,i)):
                check+=1
        # print(check)
        if check == L.size_out()-1:
            break
        if new_val:
            # print("pp")
            for i in range(L.size_out()-1):
                if find_more_than(L,i):
                    index = i
                    # print(f" index = {index},val = {L.peek(index)},next = {L.peek(index+1)}")
                    break
            # print(f" index = {index},val = {L.peek(index)},next = {L.peek(index+1)}")
            new_val = 0
        if index >-1:
            status,index = swapping(L,index)
            print(f"\nSwapping {L.peek(index)} and {L.peek(index-1)}")
            print(f"List: {L}")
            # print(new_val,index)
        if index == L.size_out()-1 or not find_more_than(L,index):
            if not find_more_than(L,index):
                if L.peek(index+1) != None and index+1 < s:
                    index = index+1
                else:
                    s-=1
                    new_val = 1
            else:
                new_val = 1
                s-=1
                # print(s)
        if check == L.size_out()-1:
            break
    print("_______________________________________")
    print(f"Sorted List: {L}")        
main()
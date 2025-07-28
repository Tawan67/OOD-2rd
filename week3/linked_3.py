<<<<<<< HEAD
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
        return ' -> '.join(ans)

    
    
    
    
    
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
        insert = self.Node(data)
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
            after = target.next # 1
            after_next = after.next # 2
            
            self.head = after # 1
            after.next = target # 1-->0
            target.next = after_next # 1-->0-->2
            
            return 1,index+1
        else:
            check = 0
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            target = prev.next
            after  = target.next
            after_next = after.next
            prev.next = after
            after.next = target
            target.next = after_next
            return 1,index+1
    def reverse(self,range_in=None,index_in=None):
        if index_in == None:
            index_in = 0
        if range_in == None:
            range_in = self.size_out()
        for i in range(range_in-1,-1,-1):
            index = index_in
            for j in range(i):
                a,index = self.r_shift(index)
        print(self) 



# input : 1 2 3
# Original
# 1 -> 2 -> 3
def sum(n:int,i=1):
    sum_val=0
    for val in range(i,n,1): #sum i to n-1
        sum_val += val
    return sum_val

def main():
    L=LinkedList()
    input1 = input("input : ")
    for i in input1.split(" "):
        if i.isnumeric(): 
            i = int(i)
        L.append(i)
    print("Original")
    print(L)
    print("\nProcess")
    for i in range(L.size_out()-1,-1,-1):
        index = 0
        for j in range(i):
            a,index = L.r_shift(index)
            print(L)
    print()
    print("Reverse")
    print(L)
main()
=======
pass
>>>>>>> fc63f87 (first recursive for week 4)

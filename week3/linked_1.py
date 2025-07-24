class Node:
    def __init__(self,data,next = None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next
            
class LinkedList:
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
    
    
    
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s
    
    
    def isEmpty(self):
        return self.size ==0
    
    def append(self,data):
        new = Node(data)
        if self.head == None:
            self.head = new
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new
        self.size += 1
    
    def addHead(self,data):
        new = Node(data)
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
        # if self.size == 0:
        #     return "Empty"
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
            return "Success"
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
               return "Success"
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




L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size_out(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
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
        return ' '.join(ans)

    
    
    
    
    
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
class Ant:
    def __init__(self):
        
        pass
    @property
    def use(self):
         pass
class WorkingAnt(Ant):
    num = 0
    amount = 0
    def __init__(self):
        WorkingAnt.num+=1
        self.name = f"W{WorkingAnt.num}" 
        self.carry = 2
        self.str = 5
        WorkingAnt.amount +=1
        
    @property
    def use(self):
        if WorkingAnt.amount > 0:
            WorkingAnt.amount-=1
            WorkingAnt.num-=1
               
    def __str__(self):
        return self.name
    
class ArmyAnt(Ant):
    amount = 0
    num_2 = 0
    def __init__(self):
        ArmyAnt.num_2+=1
        self.name = f"A{ArmyAnt.num_2}"
        self.carry = 5
        self.str = 10  
        ArmyAnt.amount+=1
    def __str__(self):
        return self.name
    
    @property
    def use(self):
        if ArmyAnt.amount > 0:
            ArmyAnt.amount-=1
            ArmyAnt.num_2-=1
            
      
def main():
    print("***This colony is our home***")
    ant_in,cm = input("Enter input : ").split("/")
    w,a = map(int, ant_in.split())
    ants = LinkedList()
    angry = 0
    for i in range(w):
        ants.append(WorkingAnt())
    for i in range(a):
        s=f"A{i+1}"
        ants.append(ArmyAnt())
    if ants.size_out()==0:
        print(f"Current Ant List: Empty\n")
    else:
        print(f"Current Ant List: {ants}\n")
    cm = cm.split(",")
    index = 0
    for i in cm:
        cm[index] = i.split(" ")
        index+=1
    pop_list = []
    # print(cm)
    for i in cm:
        sucess = 0
        if i[0]== 'C': #carry has 2 condition
            carry_ant = ""
            val = int(i[1])
            if ants.size_out() == 0: # empty list
                carry_ant="Empty"
            elif val <= WorkingAnt.amount*2: # if ant worker can handle its
                carry_ant = ""
                pop_list.clear()
                for i in range(ants.size_out()):
                    if isinstance(ants.peek(i),WorkingAnt) and val > 0:
                        carry_ant+=str(ants.peek(i))+" "
                        val-=2
                        pop_list.append(i)
                while len(pop_list)> 0:
                    death_ant = ants.pop(pop_list.pop())
                    death_ant.use
                sucess = 1
            else:
                carry_ant = ""
                pop_list.clear()
                for i in range(ants.size_out()):
                    if isinstance(ants.peek(i),WorkingAnt) and val > 0:
                        carry_ant+=str(ants.peek(i))+" "
                        val-=2
                        pop_list.append(i)
                while len(pop_list)> 0:
                    death_ant = ants.pop(pop_list.pop())
                    death_ant.use
                for i in range(ants.size_out()):
                    if val > 0:
                        carry_ant+=str(ants.peek(i))+" "
                        val-=5
                        pop_list.append(i)
                while len(pop_list)> 0:
                    death_ant = ants.pop(pop_list.pop())
                    death_ant.use
                
            
                
            print(f"Food carrying mission : {carry_ant}")
            if val > 0:
                print("The food load is incomplete!")
                print("Queen is angry! ! !")
                angry+=1
        elif i[0]== 'F':
            actack_ant = ""
            val = int(i[1])
            if ants.size_out() == 0: # empty list
                actack_ant="Empty"
            elif val <= ArmyAnt.amount*10: # if ant ARMY can handle its
                actack_ant = ""
                pop_list.clear()
                for i in range(ants.size_out()):
                    if isinstance(ants.peek(i),ArmyAnt) and val > 0:
                        actack_ant+=str(ants.peek(i))+" "
                        val-=10
                        pop_list.append(i)
                while len(pop_list)> 0:
                    death_ant = ants.pop(pop_list.pop())
                    death_ant.use
                sucess = 1
            else:
                actack_ant = ""
                pop_list.clear()
                for i in range(ants.size_out()):
                    if isinstance(ants.peek(i),ArmyAnt) and val > 0:
                        actack_ant+=str(ants.peek(i))+" "
                        val-=10
                        pop_list.append(i)
                while len(pop_list)> 0:
                    death_ant = ants.pop(pop_list.pop())
                    death_ant.use
                for i in range(ants.size_out()):
                    if val > 0:
                        actack_ant+=str(ants.peek(i))+" "
                        val-=5
                        pop_list.append(i)
                while len(pop_list)> 0:
                    death_ant = ants.pop(pop_list.pop())
                    death_ant.use
                
            
                
            print(f"Attack mission : {actack_ant}")
            if val > 0:
                print("Ant nest has fallen!")
                break
        
        elif i[0]=='S':
            s_w=""
            s_a=""
            pop_list.clear()
            for i in range(ants.size_out()):
                if isinstance(ants.peek(i),WorkingAnt):
                    s_w+=str(ants.peek(i))+" "
                if isinstance(ants.peek(i),ArmyAnt):
                    s_a+=str(ants.peek(i))+" "
            if s_w =="":
                s_w = "Empty"
            if s_a =="":
                s_a = "Empty"
            print(f"""-> Remaining worker ants: {s_w}\n-> Remaining soldier ants: {s_a}""")
        elif i[0] == 'W':
            
            for i in range(int(i[1])):
                ants.append(WorkingAnt())
        elif i[0] == 'A':
            for i in range(int(i[1])):
                ants.append(ArmyAnt())
        else:
            print("Error")
        if angry == 3:
            print("**The queen is furious! The ant colony has been destroyed**")
            break
            
                    
            
            
            
main()
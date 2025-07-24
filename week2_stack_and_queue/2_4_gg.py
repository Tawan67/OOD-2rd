class Queue:
    def __init__(self,list_in=None):
        if list_in==None:
            list_in = []
        self.queuue = list_in
        self.size = len(self.queuue)
        pass
    
    def enqueue(self,item):
        self.queuue.append(item)
        self.size+=1
    
    
    def dequeue(self):
        if self.size>0:
            self.size -=1
            return self.queuue.pop(0)
        return -1
        # print("Cant deQueue")
        # return None
    @property
    def is_empty(self):
        return self.size == 0
    @property
    def peek(self):
        if self.size_q == 0:
            return -1
        return self.queuue[0]
    @property
    def size_q(self):
        return self.size
    def __str__(self):
        ss=f"Queue size : {self.size}" + "\nList : "
        s=""
        for i in range(self.size_q):
            if i!=self.size_q-1 and i > 0:
                s+= " "+ str(self.queuue[i])+","
            elif i==0 and self.size>1:
                
                s+=str(self.queuue[i])+","
            elif i == self.size -1 and self.size>1:
                s+=" "+str(self.queuue[i])
            else:
                s+=str(self.queuue[i])
                
        if self.size == 0:
            return "None"
        return s
        pass
    @property
    def notEm(self):
        return not self.is_empty
    def reset(self):
        self.queuue.clear()
        self.size = 0
    
    def copy(self,queue:'Queue'):
        temp = Queue()
        self.reset()
        while queue.notEm:
            self.enqueue(queue.peek)
            temp.enqueue(queue.dequeue())
        while temp.notEm:
            queue.enqueue(temp.dequeue())

    def search(self,ele):
        temp = Queue()
        temp.copy(self)
        if self.size_q == 0:
            return 0
        while temp.notEm:
            if ele == temp.dequeue():
                return 1
        return 0

class Stack:
    def __init__(self,list_item = None):
        if list_item == None:
            list_item = []
        self.items = list_item
        self.size = len(self.items)
        
    def push(self,item):
        self.items.append(item)
        
        
    @property
    def pop_item(self):
        if len(self.items):
            return self.items.pop()
        print("Can't Pop It's Out of Range")
        return None
    @property
    def peek(self):
        return self.items[-1]
    @property
    def isEmpty(self):
        return len(self.items)==0
    @property
    def size_list(self):
        return len(self.items)

    def __str__(self):
        s = "stack's size is "+str(self.size_list)+ "\nlist :"
        for i in self.items:
            s += str(i)+" "
        return s+'\n'
    
    @property
    def sum(self):
        sum = 0
        try:
            for i in self.items:
                sum+=i
            return sum
        except:
            # print("This is not pure Numberic Stack")
            return 0
        
    def reset(self,re_list=None):
        if re_list == None:
            re_list = []
        self.items = re_list.copy()
    
    def copy(self,stack:"Stack"):
        self.reset()
        store_stack = Stack()
        while stack.notEm:
            store_stack.push(stack.pop_item)
        while store_stack.notEm:
            self.push(store_stack.peek)
            stack.push(store_stack.pop_item)
        return self.items
    def sort(self):
        self.items.sort()
        
    @property
    def stack_re(self):
        a = Stack()
        while self.size_list >0:
            a.push(self.pop_item)
        self.copy(a)
    @property
    def IsFloat(self):
        for i in self.items:
            if is_float(str(i)):
                return 1
        return 0
    @property
    def notEm(self):
        return not(self.isEmpty)

def main():
    text = input("Enter input: ").split(",")
    # print(text)
    paper = 3
    printing_q = Queue()
    refil = Queue()
    tray_q = Queue()
    tray = Stack()
    status = Queue()
    next = 1
    compare = 0
    oper = Queue()
    pq = Queue()
    while len(text) > 0:
        T=0
        i = text.pop(0)
        cmd,value = i.split(":",1)
        cmd = [i for i in cmd if i!= " "]
        cmd = cmd[0]
        start = list()
        word = list()
        # value = list(value)
        
        if cmd  == 'P':
            init,word = value.split(" ",1)
            init = int(init)
            word = list(word)
            printing_q.enqueue([init,word])
            T=init
        if cmd == 'S':
            T=int(value)
            status.enqueue(T)
            
        if cmd =='R':
            time,val = value.split(" ",1)
            time = int(time)
            val = int(val)
            refil.enqueue([time,val])
            T = time
        if cmd == 'T':
            T = int(value)
            tray_q.enqueue(T)
        oper.enqueue(cmd)
        if T > compare:
            compare =T 
    w_t = 0
    # print(status)
    Time = 0
    while Time < compare+1 and Time < 1000:
        purpeech = 1
        if pq.notEm and paper > 0 and purpeech:
            Time += 1
            # print("Boag")
            w_t+=1
            
            # if Time == 5:
            #     print(pq,w_t)
            if w_t - pq.peek[0] == 0:
                # print("in")
                paper -= 1
                # print(paper)
                # print(f"pop {pq.peek} time = {Time} paper still be {paper}")
                tray.push(pq.dequeue()[1])
                w_t = 0
                purpeech = 0
        if paper == 0:
            print("[Time %s] Error: Printer is out of paper. Please refill."%Time)
            purpeech = 0
        

        while ((printing_q.notEm and printing_q.peek[0] <= Time ) or 
               (status.notEm and status.peek <= Time ) or 
               (refil.notEm and refil.peek[0] <= Time  ) or 
               (tray_q.notEm and tray_q.peek <= Time )):
            
            if printing_q.notEm and oper.peek == 'P' and printing_q.peek[0] == Time:
                if pq.size_q >= 3:
                    oper.dequeue()
                    pde = printing_q.dequeue()
                    print(f"[Time {Time}] Error: Printer buffer is full. Please try again later.")
                else:
                    t = -(-len(printing_q.peek[1])//5)
                    s = ""
                    for i in printing_q.peek[1]:
                        s+= i
                    pq.enqueue([t,s])
                    
                    ode = oper.dequeue()
                    pde = printing_q.dequeue()
                    # print(f"{ode} == {pde[0]}")
                    
            if status.notEm and oper.peek == 'S' and status.peek == Time:
                if pq.is_empty:
                    print(f"[Time {Time}] Status: Idle. Pending 0 file(s) in queue.")
                else:
                    print(f"[Time {Time}] Status: Printing... \"{pq.peek[1]}\" and Pending {pq.size_q-1} file(s) in queue.")
                oper.dequeue()
                status.dequeue()   
                # print(f"{} == {}")
            if tray_q.notEm and oper.peek == 'T' and tray_q.peek == Time:
                if tray.notEm:
                    tr = ""
                    tr += '"' + tray.pop_item + '"'
                    while tray.notEm:
                        tr+= ", "+'"' + tray.pop_item+ '"'
                    print("[Time %s] You got: %s"%(Time,tr))
                      
                else:
                    print(f"[Time {Time}] You got: Nothing in tray.")
                tde = tray_q.dequeue()
                ode = oper.dequeue()
                
                # print(f"{ode} == {tde}")
            if refil.notEm and oper.peek == 'R' and refil.peek[0] == Time:
                oper.dequeue()
                paper += refil.dequeue()[1]
                # print(f"{} == {}")
                pass
            # if Time == 2:
            #     return
        Time +=1
                
main()
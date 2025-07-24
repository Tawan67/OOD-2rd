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
    # print(compare)
    # print(oper)
    #find max time
    
    for Time in range(compare): #start printer
        while ((printing_q.peek[0] <= Time and printing_q.size_q > 0 and printing_q.peek[0] != None) or 
               (status.peek <= Time and status.size_q > 0) or 
               (refil.peek <= Time and refil.size_q > 0 ) or 
               (tray_q.peek <= Time and tray_q.size_q > 0)):
            # print(printing_q.peek[0] ,f"print = {(printing_q.peek[0] <= Time and printing_q.size_q > 0)}",Time)
            #       print(status.peek),f"status = {(status.peek <= Time and status.size_q > 0)}",
            #       print(refil.peek),f"refil = {(refil.peek <= Time and refil.size_q > 0 )}",
            #       print(tray_q.peek),f"tray = {(tray_q.peek <= Time and tray_q.size_q > 0)}")
            if printing_q.notEm and(oper.peek == 'P'): # try to enqueue
                print(printing_q.peek)
                if printing_q.peek[0] == Time:
                    if pq.size_q > 2:
                        print("Fulll")
                        printing_q.dequeue()
                        oper.dequeue()
                    elif paper > 0:
                        work = printing_q.peek
                        init = work[0]
                        word_size = len(work[1])
                        s = ""
                        for i in work[1]:
                            s+=i
                        t_use = -(-word_size//5)
                        paper -= 1
                        printing_q.dequeue()
                        pq.enqueue([init,t_use,s])
                        # print(pq)
                        oper.dequeue()
                    else:
                        print("[Time %s] Error: Printer is out of paper. Please refill."%Time) # dequeue ยกเว้น กระดาษ หมด
                        oper.dequeue()
    
            if tray_q.notEm and tray_q.peek == Time and tray.notEm and oper.peek == 'T': #try to tray
                # print(tray)
                tr = ""
                tr += '"' + tray.pop_item + '"'
                while tray.notEm:
                    tr+= ", "+'"' + tray.pop_item+ '"'
                print("[Time %s] You got: %s"%(Time,tr))
                tray_q.dequeue()
                oper.dequeue()   
            elif tray_q.notEm and tray_q.peek <=Time and tray.isEmpty and oper.peek == 'T':
                print("[Time %s] You got: Nothing in tray."%Time)
                oper.dequeue()
                
            if refil.notEm and (refil.peek[0] == Time) and (oper.peek == 'R'): #paper refil
                paper += refil.dequeue()[1]
                oper.dequeue()
            
            
        if pq.notEm: # printing
            pq.peek
            pq.peek[1] -= 1
            print(pq.peek[1])
            print(pq)
            if pq.peek[1] == 0:
                print("in")
                w = pq.peek[2]
                
                tray.push(w)
                # print(w,Time,paper)
                # print(f"push {w} in tray and T = {Time}")
                pq.dequeue()
                print(pq)
                if printing_q.notEm and printing_q.peek[0] == Time and oper.peek == '':
                    work = printing_q.peek
                    init = work[0]
                    word_size = len(work[1])
                    s = ""
                    for i in work[1]:
                        s+=i
                    t_use = -(-word_size//5)
                    paper -= 1
                    printing_q.dequeue()
                    pq.enqueue([init,t_use,s])
                    print(pq)
                    break
                else:
                    print("[Time %s] Error: Printer is out of paper. Please refill."%Time) # dequeue ยกเว้น กระดาษ หมด
       
main()
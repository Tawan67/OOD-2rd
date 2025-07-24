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
    
    @property
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
        return self.queuue[0]
    @property
    def size_q(self):
        return self.size
    def __str__(self):
        ss=f"Queue size : {self.size}" + "\nList : "
        s=""
        for i in self.queuue:
            s+=str(i)+" "
        return s
        pass
    @property
    def notEm(self):
        return not self.is_empty
input = input("Enter Input : ")
opr = input.split(",")
queue = Queue()
for set in opr:
    if set == 'D':
        if (queue.notEm):
            print(f"{queue.dequeue} 0")
        else:
            print(f"{queue.dequeue}")
    else:
        cmd,value = set.split(" ")
        value = int(value)
        if cmd == 'E':
            queue.enqueue(value)
            print(queue.size_q)
if queue.is_empty:
    print("Empty")
else:
    print(queue)

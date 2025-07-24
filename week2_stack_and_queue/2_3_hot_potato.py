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
        s=str(self.queuue)

    
    
    
        return s
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
            temp.enqueue(queue.dequeue)
        while temp.notEm:
            queue.enqueue(temp.dequeue)

    def search(self,ele):
        temp = Queue()
        temp.copy(self)
        if self.size_q == 0:
            return 0
        while temp.notEm:
            if ele == temp.dequeue:
                return 1
        return 0

def main():
    print("*****Hot Potato Game*****")
    li,ro = input("Enter Input: ").split("/")
    # li,ro = input_1.split("/")
    ro = int(ro)
    li = [i for i in li.split(",")]


    players = Queue(li)
    round_ = ro
    c= 0
    if ro <0:
        print("%s is the first player holding the potato"%players.peek)
        return 0
    while players.size_q > 1:
        if round_ == ro:
            
            print("%s is the first player holding the potato"%players.peek)
            players.enqueue(players.dequeue)
            round_-=1
        elif round_ > 0:
            print("  Potato passed to: %s"%players.peek)
            players.enqueue(players.dequeue)
            round_-=1
        else:
            print("  Potato passed to: %s"%players.peek)
            print("Eliminated: %s. Remaining players: %s"%(players.dequeue,players.queuue))
            round_ = ro
            c+=1
    print()
    print(f"The winner is: {players.dequeue}!")

main()
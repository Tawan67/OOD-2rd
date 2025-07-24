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
        # for i in range(self.size_q):
        #     if i!=self.size_q-1 and i > 0:
        #         s+= " "+ str(self.queuue[i])+","
        #     elif i==0 and self.size>1:
                
        #         s+=str(self.queuue[i])+","
        #     elif i == self.size -1 and self.size>1:
        #         s+=" "+str(self.queuue[i])
        #     else:
        #         s+=str(self.queuue[i])
                
        # if self.size == 0:
        #     return "None"
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
    print(" ***Queue of Queue of Queue of ...***")
    text = input("Enter Input : ")
    li = text.split(",")
    company = Queue()
    for i in li:
        check = 1
        if " " in i:
            cmd,value = i.split(" ")
            value = int(value)
            if company.notEm:
                on = 1
                temp = Queue()
                while company.notEm:
                    for i in company.peek:
                        # print(i,"ew",value)
                        if i+1 == value:
                            # print("wisadel")
                            company.peek.append(value)
                            print(f"Enqueued: {value}")
                            on = 0
                    if not on:
                        while company.notEm:
                            temp.enqueue(company.dequeue)
                        company.copy(temp)
                        temp.reset()
                        break
                    elif company.notEm:
                        temp.enqueue(company.dequeue)
                    else:
                        company.copy(temp)
                        break
                if company.is_empty and temp.notEm:
                    company.copy(temp)       
                if on:
                    
                    company.enqueue([value])
                    print(f"Enqueued: {value}")
            else:
                company.enqueue([value])
                print(f"Enqueued: {value}")
        elif i == "de":
            if company.is_empty:
                check = 0
                print("Queue is empty")
            elif company.notEm and len(company.peek) > 1:
                a=company.peek.pop(0)
                print(f"Dequeued: {a}")
            else:
                print(f"Dequeued: {company.dequeue[0]}")
        if check :print(f"Queue state: {company}")
                
    
main()
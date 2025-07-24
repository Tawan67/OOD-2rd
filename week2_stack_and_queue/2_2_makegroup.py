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



# def cant_group(q: Queue, s: int, g: Queue) -> int:
#     # สร้างสำเนา q และ g เพื่อไม่แก้ของจริง
#     temp_q = Queue()
#     temp_q.copy(q)
    
#     group = Queue()
#     group.copy(g)

#     while group.size_q < s and temp_q.notEm:
#         color = temp_q.dequeue
#         group.enqueue(color)

#         colors = group.queuue[:group.size_q]  # คัดลอกค่าทั้งหมดในกลุ่มตอนนี้
        
#         # เงื่อนไขผิด:
#         if "Pink" in colors and "Green" in colors and "Blue" not in colors:
#             return 1  # ไม่สามารถจับกลุ่มได้
#         if "Blue" in colors and "Yellow" in colors and "Red" not in colors:
#             return 1  # ไม่สามารถจับกลุ่มได้

#     if group.size_q < s:
#         return 1  # จับกลุ่มไม่ครบ

#     return 0  # สามารถจับกลุ่มได้
   
    
    
print("***Make a group***")
text = input("Enter input : ")
size,student = text.split(",")
students = ["Green", "Red", "Blue", "Yellow","Pink"]
stds = [i for i in student.split(" ") if i!=""]

stdq = Queue(stds)
group = Queue()
size = int(size)


reject = Queue()

def main(re = 0):
    num = 0
    stoppu = 1
    # purpeech = 0
    while stdq.notEm and stoppu:
        # purpeech +=1
        # if purpeech>1000:
        #     print("1")
        #     break
        x = stdq.size_q+group.size_q+reject.size_q
        if (x < size):
            stoppu = 0
        
        if size > group.size_q :
            if not group.search(stdq.peek) or re:
                if stdq.peek == "Pink":
                    
                    if group.search("Green"):
                        if group.search("Blue"):
                            group.enqueue(stdq.dequeue)
                        else:
                            reject.enqueue(stdq.dequeue)
                    else:
                        # print("P")
                        group.enqueue(stdq.dequeue)
                        
                elif stdq.peek == "Green":
                    if group.search("Pink"):
                        if group.search("Blue"):
                            group.enqueue(stdq.dequeue)
                        else:
                            reject.enqueue(stdq.dequeue)
                    else:
                        group.enqueue(stdq.dequeue)
                elif stdq.peek == "Blue":
                    if group.search("Yellow"):
                        if group.search("Red"):
                            group.enqueue(stdq.dequeue)
                        else:
                            reject.enqueue(stdq.dequeue)
                    else:
                        group.enqueue(stdq.dequeue)
                elif stdq.peek == "Yellow":
                    if group.search("Blue"):
                        if group.search("Red"):
                            group.enqueue(stdq.dequeue)
                        else:
                            reject.enqueue(stdq.dequeue)
                    else:
                        # print("Y")
                        group.enqueue(stdq.dequeue)
                else:
                    group.enqueue(stdq.dequeue)
            else:
                reject.enqueue(stdq.dequeue)
                
                        
        if group.size_q == size:
            num+=1
            print(f"Group {num} : {group}")
            group.reset()
    
    while group.notEm:
        reject.enqueue(group.dequeue)

main(1)
# if reject.size_q >= size:
#     stdq.copy(reject)
#     reject.reset()
#     main(1)
#     pass

print(f"Rejected : {reject}")

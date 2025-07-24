class Queue:
    def __init__(self, list_in=None):
        if list_in is None:
            list_in = []
        self.queue = list_in

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty:
            return self.queue.pop(0)
        return -1

    @property
    def is_empty(self):
        return len(self.queue) == 0

    @property
    def peek(self):
        if self.is_empty:
            return -1
        return self.queue[0]

    @property
    def size_q(self):
        return len(self.queue)

    def __str__(self):
        return ', '.join(str(i) for i in self.queue) if not self.is_empty else "None"

    @property
    def notEm(self):
        return not self.is_empty

    def reset(self):
        self.queue.clear()

    def copy(self, queue: 'Queue'):
        temp = Queue()
        self.reset()
        while queue.notEm:
            self.enqueue(queue.peek)
            temp.enqueue(queue.dequeue())
        while temp.notEm:
            queue.enqueue(temp.dequeue())

    def search(self, ele):
        temp = Queue()
        temp.copy(self)
        while temp.notEm:
            if ele == temp.dequeue():
                return 1
        return 0


class Stack:
    def __init__(self, list_item=None):
        if list_item is None:
            list_item = []
        self.items = list_item

    def push(self, item):
        self.items.append(item)

    @property
    def pop_item(self):
        if self.items:
            return self.items.pop()
        return None

    @property
    def peek(self):
        return self.items[-1] if self.items else None

    @property
    def isEmpty(self):
        return len(self.items) == 0

    @property
    def size_list(self):
        return len(self.items)

    def __str__(self):
        return ', '.join(str(i) for i in self.items)

    def reset(self, re_list=None):
        if re_list is None:
            re_list = []
        self.items = re_list.copy()

    def copy(self, stack: 'Stack'):
        self.reset()
        store_stack = Stack()
        while stack.notEm:
            store_stack.push(stack.pop_item)
        while store_stack.notEm:
            self.push(store_stack.peek)
            stack.push(store_stack.pop_item)

    def sort(self):
        self.items.sort()

    @property
    def stack_reverse(self):
        a = Stack()
        while self.size_list > 0:
            a.push(self.pop_item)
        while a.notEm:
            self.push(a.pop_item)

    @property
    def notEm(self):
        return not self.isEmpty


def main():
    text = input("Enter input: ").split(",")
    printing_q = Queue()
    refil = Queue()
    tray_q = Queue()
    tray = Stack()
    status = Queue()
    oper = Queue()
    pq = Queue()
    paper = 3
    max_time = 0

    for cmd in text:
        cmd = cmd.strip()
        T = 0
        try:
            cmd,val = text.split(" ")
        except:
            val=None
        
            pass   
    while Time <= max_time or not pq.is_empty:
        while refil.notEm and refil.peek[0] == Time:
            _, amount = refil.dequeue()
            paper += amount
            oper.dequeue()

        while printing_q.notEm and printing_q.peek == Time:
            printing_q.dequeue()
            oper.dequeue()

        while status.notEm and status.peek == Time:
            if pq.is_empty:
                print(f"[Time {Time}] Status: Idle. Pending 0 file(s) in queue.")
            else:
                current = pq.peek[1]
                print(f"[Time {Time}] Status: Printing... \"{current}\" and Pending {pq.size_q-1} file(s) in queue.")
            status.dequeue()
            oper.dequeue()

        while tray_q.notEm and tray_q.peek == Time:
            if tray.notEm:
                tray.stack_reverse
                output = []
                while tray.notEm:
                    output.append(f'"{tray.pop_item}"')
                print(f"[Time {Time}] You got: {', '.join(output)}")
            else:
                print(f"[Time {Time}] You got: Nothing in tray.")
            tray_q.dequeue()
            oper.dequeue()

        # print only one per time
        if pq.notEm and printing_q.search(Time):
            if paper == 0:
                print(f"[Time {Time}] Error: Printer is out of paper. Please refill.")
            else:
                paper -= 1
                tray.push(pq.dequeue()[1])

        Time += 1

main()

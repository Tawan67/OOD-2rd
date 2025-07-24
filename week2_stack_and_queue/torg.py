class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else: 
            self.items = list

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        try:
            return self.items.pop(0)
        except IndexError:
            return "Empty"

    @property
    def size(self):
        return len(self.items)

    def __str__(self):
        if self.isEmpty():
            return "None"

        s = "\""
        for i in range(len(self.items)):
            s += str(self.items[i])
            try: 
                if self.items[i+1] != None:
                    s += "\", \""            
            except IndexError:
                break
        s += "\""
        return s

class Stack:
    total = 0 
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else: 
            self.items = list

        self.size = len(self.items)
        Stack.total += 1

    def push(self, i ):
        self.items.append(i)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.items.pop()

    def peek(self):
        return self.items[-1]        

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        if self.isEmpty():
            return "None"

        s = "\""
        for i in range(len(self.items)):
            s += str(self.items[i])
            try: 
                if self.items[i+1] != None:
                    s += "\", \""            
            except IndexError:
                break
        s += "\""
        return s

# status = Queue()
previous_line = ""
next_line = ""
pending = Queue()
paper = 3
tray = Queue()
status = ""

pairs = input("Enter input: ").split(", ")
print(pairs)
commands = []
value = []
for i in pairs:
    commands.append(i.split(" ")[0])
    try:
        value.append(i.split(" ")[1])
        for j in range(2, len(i.split(" "))):
            value[-1] += " "
            value[-1] += i.split(" ")[j]
    except IndexError:
        value.append(None)
# print(value)
# S,T Value == None
max_second = int(commands[-1].split(":")[1])
#time ตัวสุดท้าย
for second in range(max_second+1):

    previous_line += status

    if next_line != "":
        status = next_line[0:5]
        next_line = next_line[5:] if len(next_line) > 5 else ""

    elif next_line == "" and previous_line != "":
        tray.enqueue(previous_line)
        paper -= 1
        if pending.isEmpty():
            status = ""
        elif paper > 0:
            status = pending.dequeue()
            if len(status) > 5:
                next_line = status[5:]
                status = status[0:5]
        elif paper == 0:
            status = ""
        previous_line = ""

    elif previous_line == "" and next_line=="" and status == "" and paper != 0 and not pending.isEmpty():
        status = pending.dequeue()
        if len(status) > 5:
            next_line = status[5:]
            status = status[0:5]

    this_second_command_list = Queue()
    for i, command in enumerate(commands):
        command_second = int(command.split(":")[1])
        if command_second == second:
            this_second_command_list.enqueue([command,value[i]])

    for second_command in this_second_command_list.items:
        operation = second_command[0].split(":")[0]

        if operation == "S":
            if paper == 0:
                print("[Time %d] Error: Printer is out of paper. Please refill."%second)
            elif status == "":
                print("[Time %d] Status: Idle. Pending %d file(s) in queue."% (second,pending.size))
            else:
                print("[Time %d] Status: Printing... \"%s\" and Pending %d file(s) in queue."% (second, previous_line+status+next_line,pending.size))

        elif operation == "P":
            if paper == 0:
                pending.enqueue(second_command[1])
                print("[Time %d] Error: Printer is out of paper. Please refill."%second)
            elif status == "":
                status = second_command[1][0:5]
                if len(second_command[1]) > 5:
                    next_line = second_command[1][5:]
            else:
                if pending.size < 3:
                    pending.enqueue(second_command[1])
                else:
                    print("[Time %d] Error: Printer buffer is full. Please try again later."%second)

        elif operation == "T":
            if paper == 0 and pending.size != 0:
                print("[Time %d] Error: Printer is out of paper. Please refill."%second)
            stack = Stack()
            count = tray.size
            for _ in range(count):
                stack.push(tray.dequeue())
            for _ in range(count):
                tray.enqueue(stack.pop())
            if tray.size == 0:
                print("[Time %d] You got: Nothing in tray."%second)
            else:
                print("[Time %d] You got: %s"% (second, tray))
            tray.items = []

        elif operation == "R":
            if paper == 0:
                status = pending.dequeue()
                if len(status) > 5:
                    next_line = status[5:]
                    status = status[0:5]
            paper += int(second_command[1])
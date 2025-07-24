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
def reverse(string:str):
    i = [i+']' for i in string.split("]")]
    i.reverse()
    i=[j for j in i if j!=']']
    i = "".join(i)
    return i
    
def is_float(element):
    if not("." in element):
        return 0
    for i in element:
        if i == '.':
            initial  = element.index(i)
            try:
                if not(element[initial-1].isnumeric() and element[initial+1].isnumeric()):
                    return 0
            except:
                return 0
    return 1


input_text = input("Enter needed weight(s): ")
check = True
sticks =[]
for i in input_text:
    if i ==" ":
        stick_base = input_text.split(" ")
        for i in stick_base:
            if is_float(i):
                sticks.append(float(i))
            else:
                sticks.append(int(i))
        check = False
        break
if check:
    if(is_float(input_text)):
        sticks.append(float(input_text))
    else:
        sticks.append(int(input_text))


plate_list = [1.25,2.5,5,10,15,20,25]
plate = Stack(plate_list)

current = Stack()
past = Stack()
temp = Stack()
p_o = Stack()
p_u = Stack()

for i in sticks:
    plate.reset(plate_list)
    now = i
    previous = past.sum
    side = (i-20)/2
    part =side
    #plate in
    # print("start",current)
    while current.sum != side and plate.notEm:
        if plate.notEm and plate.peek <= part and current.sum < side: # part is is side but can change
            part -= plate.peek
            current.push(plate.peek)
            p_u.push(plate.peek)
        else:
            if current.sum == side:
                break
            if plate.notEm : plate.pop_item
        # print(current.sum," ",side)

    # print("past is ",past)
    cur_temp =Stack()
    past_temp =Stack()
    
    if current.sum < past.sum:
        cur_temp.copy(current)
        past_temp.copy(past)
        while cur_temp.notEm and past_temp.notEm:
            # print("Ew")
            while past_temp.notEm and (cur_temp.peek < past_temp.peek):
                p_o.push(past_temp.pop_item)
            cur_temp.pop_item
            
        if p_o.sum + current.sum < past.sum:
            past_t = Stack()
            for i in range(past.size_list-1):
                
                cur_temp.copy(current)
                past_temp.copy(past)
                for j in range(i+1):
                    # print(past_temp.peek)
                    past_t.push(past_temp.pop_item)
                while cur_temp.notEm and past_temp.notEm:
            # print("Ew")
                    while past_temp.notEm and (cur_temp.peek < past_temp.peek):
                        p_o.push(past_temp.pop_item)
                    cur_temp.pop_item
                if p_o.sum + current.sum >= past.sum:
                    while past_t.notEm:
                        p_o.push(past_t.pop_item)
                        p_o.sort()
                    break
                # print("re",p_o.sum,current.sum,past.sum)
                p_o.reset()
            # print(p_o)    
            # print("Lower")
            
    if current.sum > past.sum:
        cur_temp.copy(current)
        past_temp.copy(past)
        while cur_temp.notEm and past_temp.notEm:
            # print("Ew")
            while past_temp.notEm and (cur_temp.peek > past_temp.peek):
                p_o.push(past_temp.pop_item)
            cur_temp.pop_item
    # print("current is",current,"PO is",p_o,"PU is",p_u,"Past is",past,"\neiei")
    
    # if current.sum+p_o.sum != past.sum and past.sum > current.sum:
        
    #     past_temp.copy(past)
    #     print("past",past,"past_temp",past_temp)
        
    #     while p_o.isEmpty or current.sum+p_o.sum != past.sum and past_temp.notEm:
    #         # print("90")
    #         if past_temp.notEm :p_o.push(past_temp.pop_item)
    pu_temp =Stack()
    pu_temp.copy(p_u)
    p_u.stack_re
    past_temp.copy(past)
    past_temp.stack_re
    # print("PU =",p_u,"Po =",p_o)
    while (side > 0 and past_temp.notEm and p_u.peek == past_temp.peek) or (p_o.notEm and p_u.peek == p_o.peek):
        if p_o.notEm and p_u.peek == p_o.peek:
            p_o.pop_item
        p_u.pop_item
        past_temp.pop_item
    if side == 0 and past.sum > 0:
        p_o.copy(past)
        p_o.stack_re
    # while p_o.notEm and p_u.peek == p_o.peek:
    #     p_u.pop_item
    #     p_o.pop_item
    p_u.stack_re
    po_temp = Stack()
    # po_temp.copy(p_o)
    # print("PO temp",po_temp)
    
    #print ละเด้ออออ
    
    front = ""
    while not(p_o.isEmpty):
        po_temp.push(p_o.pop_item)
    while not(po_temp.isEmpty):
        front+= "PO:"+str(po_temp.pop_item)+" "
    
    pu_temp.copy(p_u)
    pu_temp.stack_re
    while not(pu_temp.isEmpty):
        front+= "PU:"+str(pu_temp.pop_item)+" "
    
    current_temp = Stack()
    current_temp.copy(current)
    output =""
    output2 = ""
    while not(current_temp.isEmpty):
        output+= '['+str(current_temp.pop_item)+']'
        output2 = reverse(output)
    bar =""
    for i in range(5-current.size_list):
        bar+="-"
   
    if side != current.sum and len(sticks) > 0 or current.size_list > 5:
        print(f"It's impossible to achieve the weight you want({now}).")
        break
    if side == 0 and past.size_list ==0:
        print(f"{front}{bar}{output}|======|{output2}{bar} => {now} KG.")
        
    elif is_float(str(current.sum)):
        print(f"{front}=> {bar}{output}|======|{output2}{bar} => {now:.1f} KG.")
    else:
        print(f"{front}=> {bar}{output}|======|{output2}{bar} => {now} KG.")
    
    
    # print("PO last",p_o)        
    p_u.reset()
    p_o.reset()
    past.copy(current)
    # print("past and future ",past)
    current.reset()
    # print("end")
    
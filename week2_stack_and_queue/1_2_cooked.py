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
        return s
    
    @property
    def sum(self):
        sum = 0
        try:
            for i in self.items:
                sum+=i
            return sum
        except:
            print("This is not pure Numberic Stack")
            return None
        
    def reset(self,re_list=None):
        if re_list == None:
            re_list = []
        self.items = re_list.copy()
    
    def copy(self,stack:"Stack"):
        self.reset()
        store_stack = Stack()
        while not(stack.isEmpty):
            self.push(stack.peek)
            store_stack.push(stack.pop_item)
        while not(store_stack.isEmpty):
            stack.push(store_stack.pop_item)
    
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
    end = i
    i=(i-20)
    i=(i/2)
    initial = i
    # if not(current.isEmpty):print(current.peek," === ",(end-((past.sum*2)+20))/2)
    if not(current.isEmpty) and (end-((past.sum*2)+20))/2 == current.peek:
        # p_o.reset()
        # p_o.push(current.pop_item)
        current.reset()
    
    if end > 250:
        print(f"It's impossible to achieve the weight you want({end}).")
        break
        
    plate.reset(plate_list)
    if not(past.isEmpty) and not(current.isEmpty):
        if i > past.sum:
            i-=past.sum
        elif i < past.sum:
            current.reset()
            pass
    count = 0
    while i > 0:
        if not(plate.isEmpty) and i>= plate.peek :
            # if not(temp.isEmpty) and i > temp.peek:
            #     i-=temp.peek
            #     p_u.push(temp.peek)
            #     plate.push(temp.pop_item)
            if count>5:
                print(f"It's impossible to achieve the weight you want({end}).")
                break
            count+=1
            i-=plate.peek
            p_u.push(plate.peek)
            current.push(plate.peek)
        else:
            temp.push(plate.pop_item)
    bar = ""
    for i in range(5-current.size_list):
            bar+='-'
    if count > 5:break       
    if not(past.isEmpty): # check which plate have to out org
        past_temp = Stack()
        pu_temp = Stack()
        past_temp.copy(past)
        pu_temp.copy(p_u)
        temp2 = Stack()
        # print("lllllllllllllll")
        # print(pu_temp.peek,end=" == ")
        # print(past_temp.peek)
        while not(pu_temp.isEmpty):
            if past_temp.peek < pu_temp.peek:
                if past_temp.isEmpty:
                    break
                p_o.push(past_temp.pop_item)
                if past_temp.isEmpty:
                    break
            else:
                if not(pu_temp.isEmpty):
                    temp2.push(pu_temp.pop_item)
            
                
        while ((p_u.sum+past.sum)-p_o.sum != current.sum) and not(past_temp.isEmpty):
            p_o.push(past_temp.pop_item)
                
        
    front =""
    p_u2 = Stack() 
    p_o2 = Stack() #reverse and add PU
    p_o2.reset()
    # print(f"{i} == {p_o} == {p_u}")
    p_u2.copy(p_u)
    p_u2.stack_re
    if not (p_o.isEmpty) and not(p_u.isEmpty) and p_u2.peek == p_o.peek:
        p_o.pop_item
        p_u2.pop_item
        p_u2.stack_re
        p_u.copy(p_u2)
    
    while not(p_o.isEmpty):
        p_o2.push(p_o.pop_item)
    while not(p_o2.isEmpty):
        front+= "PO:"+str(p_o2.pop_item)+" "
        
   #reverse and add PU
    p_u2.reset()
    while not(p_u.isEmpty):
        p_u2.push(p_u.pop_item)
    while not(p_u2.isEmpty):
        front+= "PU:"+str(p_u2.pop_item)+" "
        
    current_temp = Stack()
    current_temp.copy(current)
    output =""
    output1 = ""
    while not(current_temp.isEmpty):
        output+= '['+str(current_temp.pop_item)+']'
        output1 = reverse(output)
    
    if initial != current.sum and len(sticks) > 0 or count > 5:
        print(f"It's impossible to achieve the weight you want({end}).")
        break
    # print(p_o)
    # print(p_u)
    # print(current)
    if current.IsFloat:
        end = f"{end:.1f}"
    print(f"{front}=> {bar}{output1}|======|{output}{bar} => {end} KG.")
    
    past.copy(current)
    p_o.reset()
    p_u.reset()
    # current.reset()





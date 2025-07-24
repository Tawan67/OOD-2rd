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
    def is_in(self,ele):
        return ele in self.items
    def __str__(self):
        s = "stack of "+str(self.size_list)+ "\nlist :"
        for i in self.items:
            s += str(i)+" "
        return s
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
    def notEm(self):
        return not self.isEmpty
    def sort(self):
        self.items.sort()
    def copy(self,stack:"Stack"):
        self.reset()
        store_stack = Stack()
        while stack.notEm:
            store_stack.push(stack.pop_item)
        while store_stack.notEm:
            self.push(store_stack.peek)
            stack.push(store_stack.pop_item)
        
    def a_del(self,ele):
        for i in range(len(self.items)):
            if ele == self.items[i]:
                self.items.pop(i)
                return 0
    def more_then(self,ele):
        out_list = []
        for i in self.items:
            if ele > i:
                out_list.append(i)
        return out_list
    
    @property
    def stack_re(self):
        a = Stack()
        while self.size_list >0:
            a.push(self.pop_item)
        self.copy(a)
        return a
        
    @property
    def IsFloat(self):
        for i in self.items:
            if is_float(str(i)):
                return 1
        return 0
    
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
last = []
value = 0

def reverse(string:str):
    i = [i+']' for i in string.split("]")]
    i.reverse()
    i=[j for j in i if j!=']']
    i = "".join(i)
    return i

def out(ans:Stack,initial,before:Stack):
    # print("start")

    output = ""
    front = ""
    # check = len(last)>0
    
    end = (ans.sum()*2)+20
    before_temp =Stack()
    ans_temp = Stack()
    
    before_temp.copy(before)
    ans_temp.copy(ans) #store 1 
    # print("??????????????????")
    # print(store_1)
    # print(store_2)
    # print("////////////////////")
    
    if not(before.isEmpty): # check which plate have to out org
        past_temp = Stack()
        pu_temp = Stack()
        past_temp.copy(before)
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
            
                
        while ((p_u.sum()+before.sum())-p_o.sum() != ans.sum()) and not(past_temp.isEmpty):
            p_o.push(past_temp.pop_item)
    

    
    before1 =Stack()
    before1.copy(before)
    current1 =Stack()
    current1.copy(ans)
    
    # while not(before_temp.isEmpty) or not(ans_temp.isEmpty):
    #     if not(ans_temp.isEmpty) and not(before1.is_in(ans_temp.peek)):
    #         p_u.push(ans_temp.pop_item)
    #     elif not(ans_temp.isEmpty) :
    #         before1.a_del(ans_temp.peek)
    #         ans_temp.pop_item
            
    #     if not(before_temp.isEmpty) and not(current1.is_in(before_temp.peek)):
    #         p_o.push(before_temp.pop_item)
    #     elif not(before_temp.isEmpty):
    #         current1.a_del(before_temp.peek)
    #         before_temp.pop_item
    if not(p_o.isEmpty):
        po_temp = Stack()
        while not(p_o.isEmpty):po_temp.push(p_o.pop_item)
        while not(po_temp.isEmpty): front+= "PO:"+str(po_temp.pop_item)+" "

    p_u2 = Stack()
    p_u2.reset()
    while not(p_u.isEmpty):
        p_u2.push(p_u.pop_item)
    while not(p_u2.isEmpty):
        front+= "PU:"+str(p_u2.pop_item)+" "
    ans_temp.copy(ans)
    while not(ans_temp.isEmpty):
        output+= '['+str(ans_temp.pop_item)+']'
        output1 = reverse(output)
        bar = ""
        for i in range(5-ans.size_list):
            bar+='-'
    if(ans_temp.isEmpty and initial == 0):
        bar = "-----"
        output=""
        output1=""
        
    # print(p_o)
    if before.isEmpty and ans.isEmpty :
        print(f"{front}{bar}{output1}|======|{output}{bar} => {end} KG.")
    else:
        print(f"{front}=> {bar}{output1}|======|{output}{bar} => {end} KG.")
    # print("STOP")
    pass


plate_list = [1.25,2.5,5,10,15,20,25]
plate = Stack(plate_list)
ans = Stack()
store = Stack()
p_o = Stack()
p_u = Stack()
before = Stack()

def advice_plate(i):
    
    defult = i
    previous = (before.sum*2)+20
    if i > 250:
        print(f"It's impossible to achieve the weight you want({defult}).")
        return 0 
    
    before.copy(ans)
    
    plate.reset(plate_list)
    ans.reset()
    # print(plate)
    while not(store.isEmpty):
        plate.push(store.pop_item)
    plate.sort()
    
    #     print("-----|======|----- => 20 KG.")
    #     return 1
    i = i-20 # del stick weight for 20 kg
    i=i/2
    check = i
    if i == 0:
        
        out(ans,check,before)
        return 1
    while (i > 0) and not(plate.isEmpty):
        
        if i >= plate.peek:
            i -= plate.peek
            if(i >= plate.peek):
                ans.push(plate.peek)
                
                p_u.push(plate.peek)
            else:
                p_u.push(plate.peek)
                ans.push(plate.pop_item)
            
        else:
            plate.pop_item
            
        if check == ans.sum():
            out(ans,check,before)
            return 1
        
    
    if check != ans.sum() and len(sticks) > 0:
        print(f"It's impossible to achieve the weight you want({defult}).")
        return 0

#main

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




for i in range(len(sticks)):
    # if i!= 0 and sticks[i]==sticks[i-1]:
    #     continue
    if advice_plate(sticks[i]) == 0:
        break
    # print(f"status = {advice_plate(i)}")

# มีทางแก้ 2 ทางที่คิดไว้ 1 คือทำตัวเก็บค่าก่อนหนเ้าแล้วค่อยมาดูว่าอันไหนจะเอาเข้าหรือเอาออก
# 2  คือ ไม่ reset ค่าของ ans แล้ว เอาค่า sum ออกมา จากนั้นเอาไปเช็คกับค่า input ว่าขาดหรือเกิน ถ้าขาดให้ push เข้า ถ้าเกิน ให้ pop ออก จนกว่าจะน้อยกว่า แล้วเรียงค่าใน plate 
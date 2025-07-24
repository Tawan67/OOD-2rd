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
            print("This is not pure Numberic Stack")
            return None
        
    def reset(self,re_list=None):
        if re_list == None:
            re_list = []
        self.items = re_list.copy()
    
    def sort(self):
        self.items.sort()
    
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
def out(ans:Stack):
    output = ""
    front = ""
    check = len(last)>0
    end = (ans.sum()*2)+20
    while not(ans.isEmpty):
        if check:
            for i in range(len(last)):
                front += "PO:"+str(last.pop(i-1))+" "
        output+= '['+str(ans.peek)+']'
        front += "PU:"+str(ans.peek)+" "
        last.append(ans.pop_item)
    print(f"{front}=> ----{output}|======|{output}---- => {end} KG.")
    pass

plate_list = [1.25,2.5,5,10,15,20,25]
plate = Stack(plate_list)
ans = Stack()

def advice_plate(i):
    plate.reset(plate_list)
    ans.reset()
    # print(plate)
    if i == 20:
        print("-----|======|----- => 20 KG.")
        return 1
    i = i-20 # del stick weight for 20 kg
    i=i/2
    check = i   
    while i > 0 and not(plate.isEmpty):
        if i >= plate.peek:
            i -= plate.peek
            ans.push(plate.pop_item)
        else:
            plate.pop_item
        if check == ans.sum():
            out(ans)
            return 1
    if check != ans.sum and len(sticks) > 0:
        print(f"It's impossible to achieve the weight you want({(check*2)+20}).")
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




for i in sticks:
    # print(i)
    advice_plate(i)
    # print(f"status = {advice_plate(i)}")

# มีทางแก้ 2 ทางที่คิดไว้ 1 คือทำตัวเก็บค่าก่อนหนเ้าแล้วค่อยมาดูว่าอันไหนจะเอาเข้าหรือเอาออก
# 2  คือ ไม่ reset ค่าของ ans แล้ว เอาค่า sum ออกมา จากนั้นเอาไปเช็คกับค่า input ว่าขาดหรือเกิน ถ้าขาดให้ push เข้า ถ้าเกิน ให้ pop ออก จนกว่าจะน้อยกว่า แล้วเรียงค่าใน plate 
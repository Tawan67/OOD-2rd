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
        ss = "stack's size is "+str(self.size_list)+ "\nlist :["
        s="["
        for i in range(self.size_list):
            if i == 0 and self.size_list-1 >0:
                s+= str(self.items[i])+","
            elif i==0:
                s+=str(self.items[i])
            elif i == self.size_list - 1:
                s+= " "+str(self.items[i])
            else:
                s += " "+str(self.items[i])+","
        return s+']'
    
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
    # @property
    # def IsFloat(self):
    #     for i in self.items:
    #         if is_float(str(i)):
    #             return 1
    #     return 0
    @property
    def notEm(self):
        return not(self.isEmpty)
    
    def is_have(self,ele):
        cp = Stack()
        cp.copy(self)
        while cp.notEm:
            if cp.peek == ele:
                return 1
            else:
                cp.pop_item
        return 0
    

print("******** Parking Lot ********")
input = input("Enter max of car,car in soi,operation : ")
size,car_list,command,target = input.split(" ")
if car_list =='0':
    soi_a = Stack()
else:
    cars = [int(i) for i in car_list.split(',')]
    soi_a = Stack(cars)
    
soi_b = Stack()
size = int(size)
target = int(target)
if command == "arrive":
    if soi_a.is_have(target):
        print(f"car {target} already in soi")
    elif size <= soi_a.size_list:
        print(f"car {target} cannot arrive : Soi Full")
    else:
        soi_a.push(target)
        print(f"car {target} arrive! : Add Car {target}")
    
elif command == "depart":
    if size < soi_a.size_list:
        print(f"car {target} cannot depart : Soi Full")
    if soi_a.isEmpty:
        print(f"car {target} cannot depart : Soi Empty")
    elif not soi_a.is_have(target):
        print(f"car {target} cannot depart : Dont Have Car {target}")
    else:
        while target != soi_a.peek:
            soi_b.push(soi_a.pop_item)
        while soi_a.notEm and soi_a.peek == target :soi_a.pop_item
        while soi_b.notEm:
            soi_a.push(soi_b.pop_item)
        print(f"car {target} depart ! : Car {target} was remove")
print(soi_a)
    
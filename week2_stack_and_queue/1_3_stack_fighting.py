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
        s = str(self.items)
        return s
    @property
    def notEm(self):
        return not self.isEmpty
    
input_text = input("Enter Input : ")
start,post = input_text.split("/")
try :
    start = [int(i) for i in start.split(" ")]
    for i in start:
        if i == 0:
            start.pop(start.index(i))
except:
    start = "NoInput"
command = [i for i in post.split(",")]

if start != "NoInput":stack = Stack(start)
else:stack = Stack()
print("\nstart")
print(stack)
print()
for i in command:
    spell,value = i.split(" ")
    value = int(value)
    if value <= 0:
        print("Invalid number")
        continue
    if spell =="spawn":
        stack.push(value)
        print(f"spawn an enemy of {value} HP")
        print(stack)
        print()
    if spell == "dmg":
        killed = 0
        dmg =value
        while value >0:
            if stack.notEm and value >= stack.peek:
                value -=stack.pop_item
                killed+=1
            elif(stack.notEm) :
                enemy = stack.pop_item - value
                stack.push(enemy)
                value = 0
            if stack.isEmpty:
                value =0
        print(f"deal {dmg} damage, killed {killed} enemy")
        print(stack)
        print()
        if stack.size_list ==0:
            print(">>>> Player Wins <<<<")
            break

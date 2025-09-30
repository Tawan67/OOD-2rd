class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


def hash(key,data,table,max_quadratic):
    quadratic = 0
    size = len(table)
    key_value = 0
    for i in key:
        key_value += ord(i)
    index = key_value%size
    while table[index] != None:
        index = (key_value+pow(quadratic,2))%size
        if table[index] == None:
            new_data = Data(key,data)
            table[index] = new_data
            return 1,table
        else:
            print(f"collision number {quadratic+1} at {index}") ##เพราะเราบวกเข้าเลยตั้งแต่มันเข้า while ค่ามันเลยเป็นค่า 0 ตั้งแต่แรก ต้อง+1
            quadratic+=1
            if quadratic == max_quadratic:
                print("Max of collisionChain")
                return -1,table
    if table[index] == None:
            new_data = Data(key,data)
            table[index] = new_data
            
    return 0,table

def is_in(table,key):
    for i in table:
        if i.key == key:
            return True
    return False

print(" ***** Fun with hashing *****")
table_details,inp = input("Enter Input : ").split("/")
size,max_quadratic = map(int,table_details.split(" "))
table = [None]*size
for i in inp.split(","):
    key,data = i.split(" ")
    status,new_table = hash(key,data,table,max_quadratic)
    table = new_table.copy()
    for j in range(len(table)):
        print(f"#{j+1}	{table[j]}")
    print("---------------------------")
    if not None in table:
        print("This table is full !!!!!!")
        break
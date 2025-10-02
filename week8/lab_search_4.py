def rehash_j(table,data_in):
    old_size = len(table)
    new = next_prime(old_size)
    
    new_table = [None]*new
    data = [i for i in table if i != None]
    data.append(data_in)
    for i in data:
        index = hash(i,new_table,99)
        new_table[index] = i
    return new_table
    
def next_prime(old_size):
    new_size = (old_size*2)+1
    # return new_size
    while not is_prime(new_size):
        new_size+=2
    return new_size
def is_prime(num):
    if num%2 == 0 and num != 2:
        return False
    elif num == 3 or num == 2:
        return True
    else:
        i = 3
        while i*i <= num:
            if num%i == 0:
                return False
            i+=2
    return True

def hash(key,table,max_quadratic):
    quadratic = 0
    size = len(table)
    key_value = key
    data = key
    over = 0
    index = key_value%size
    over_value = max_quadratic
    while table[index] != None:
        over += 1
        global temp_con_details
        temp_con_details.append([over,index])
        if over >= over_value:
            return -1
        index = (key_value+pow(quadratic,2))%size
        if table[index] == None:
            return index
    if table[index] == None:
            new_data = data
            table[index] = new_data
    return index

def is_in(table,key):
    for i in table:
        if i.key == key:
            return True
    return False
temp_con_details = []
def main():
    print(" ***** Rehashing *****")
    setup,inp = input("Enter Input : ").split("/")
    inp = [int(i) for i in inp.split(" ")]
    setup = [int(i) for i in setup.split(" ")]
    table = [None]*setup[0]
    max_con = setup[1]
    threshold = (setup[2]*setup[0])/100
    print("Initial Table :")
    for i in range(len(table)):
        print("#{}	{}".format(i+1,table[i]))
    print("----------------------------------------")

    for key in inp: # key is data
        print("Add : {}".format(key))
        index = hash(key,table,max_con)
        global temp_con_details
        
        for i in temp_con_details:
            # details = temp_con_details.pop(0)
            details = i[:]
            
            # text = ("collision number {}".format(details[0]))
            # text_1 = (" at {}".format(details[1]))
            # print(text,end=text_1+"\n")
        
        if index < 0:
            print("****** Max collision - Rehash !!! ******")
            table = rehash_j(table,key)[:]
        elif index > threshold:
            print("****** Data over threshold - Rehash !!! ******")
            table = rehash_j(table,key)[:]
        else:
            table[index] = key
        for items in range(len(table)):
            print("#{}	{}".format(items+1, table[items]))
        print("----------------------------------------")

main()
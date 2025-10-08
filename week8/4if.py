def rehash_j(table,size):
    old_size = size
    new_size = next_prime(old_size)
    new_table = [None] * new_size
    data = [i for i in table if i is not None]
    
    for item in data:
        index = hash_func(item, new_table, 99)
        new_table[index] = item
    return new_table

def next_prime(n):
    candidate = (n * 2) + 1
    while not is_prime(candidate):
        candidate += 2
    return candidate

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def hash_func(key, table, max_quadratic):
    quadratic = 1
    size = len(table)
    index = key % size
    collisions = 0
    while table[index] is not None:
        collisions += 1
        print("collision number {} at {}".format(collisions, index))
        if collisions >= max_quadratic:
            return -1
        
        index = (key + (quadratic * quadratic)) % size
        quadratic += 1
    return index

def main():
    print(" ***** Rehashing *****")
    setup, inp = input("Enter Input : ").split("/")
    inp = [int(i) for i in inp.split()]
    setup = [int(i) for i in setup.split()]
    table = [None] * setup[0]
    max_con = setup[1]
    threshold = setup[2]/ 100.0
    print("Initial Table :")
    for i in range(len(table)):
        print("#{}\t{}".format(i + 1, table[i]))
    # print(threshold)
    print("----------------------------------------")
    temp_table = []
    for key in inp:
        print("Add : {}".format(key))
        index = hash_func(key, table, max_con)
        temp_table.append(key)
        if index < 0:
            print("****** Max collision - Rehash !!! ******")
            table = rehash_j(temp_table,len(table))
        else:
            
            load = (sum(1 for x in table if x is not None)+1) / float(len(table))
            # print(load)
            if load > threshold:
                print("****** Data over threshold - Rehash !!! ******")
                table = rehash_j(temp_table,len(table))
            else:
                table[index] = key
        for i in range(len(table)):
            print("#{}\t{}".format(i + 1, table[i]))
        print("----------------------------------------")
main()
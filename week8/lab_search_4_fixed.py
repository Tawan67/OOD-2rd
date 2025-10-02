def rehash_j(table, data_in):
    try:
        old_size = len(table)
        new = next_prime(old_size)
        new_table = [None] * new
        # Gather all existing data (skip None)
        data = [i for i in table if i is not None]
        data.append(data_in)
        for i in data:
            # Insert each item into new_table
            hash_result, temp_table, _ = hash_func(i, new_table, 99)
            new_table = temp_table
        return new_table
    except Exception as e:
        # print("Error in rehash_j:", e)
        return [None] * ((len(table) * 2) + 1)

def next_prime(old_size):
    new_size = (old_size * 2) + 1
    while not is_prime(new_size):
        new_size += 2
    return new_size

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
    quadratic = 0
    size = len(table)
    key_value = key
    data = key
    over = 0
    index = key_value % size
    over_value = max_quadratic
    while table[index] is not None:
        over += 1
        if over >= over_value:
            return -1, table, over_value <= over
        index = (key_value + pow(quadratic, 2)) % size
        if table[index] is None:
            table[index] = data
            return 1, table, over <= over_value
        else:
            if quadratic == max_quadratic:
                return -1, table, over <= over_value
        quadratic += 1
    if table[index] is None:
        table[index] = data
    return 0, table, over <= over_value

def is_in(table, key):
    for i in table:
        if i is not None and i == key:
            return True
    return False

print(" ***** Rehashing *****")
setup, inp = input("Enter Input : ").split("/")
inp = [int(i) for i in inp.split(" ")]
setup = [int(i) for i in setup.split(" ")]
table = [None] * setup[0]
max_con = setup[1]
threshold = (setup[2] * setup[0]) / 100.0
print("Initial Table :")
for i in range(len(table)):
    print("#{}	{}".format(i + 1, table[i]))
print("----------------------------------------")

for key in inp:
    print("Add : {}".format(key))
    error, temp_table, over = hash_func(key, table, max_con)
    if key > threshold:
        print("****** Data over threshold - Rehash !!! ******")
        table = rehash_j(table, key)
    elif error == -1:
        print("****** Max collision - Rehash !!! ******")
        table = rehash_j(table, key)
    else:
        table = temp_table
    for items in range(len(table)):
        print("#{}	{}".format(items + 1, table[items]))
    print("----------------------------------------")
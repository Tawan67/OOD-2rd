def rehash(table):
    pass
def next_prime(old_size):
    new_size = (old_size*2)+1
def is_prime(num):
    if num%2 == 0 and num != 2:
        return False
    elif num == 3 or num == 2:
        return True
    else:
        i = 3
        while i*i >= num:
            if num%i == 0:
                return False
            i+=2
    return 1
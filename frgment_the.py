def triple(n:int,pow=3):
    store = 1
    for i in range(pow):
        store = store*n
    return store
def cube_root(x):
    if x >= 0:
        return x ** (1/3)
    else:
        return -(-x) ** (1/3)  # handle negative numbers properly


len = int(input("input you range; "))
for i in range(len):
    for j in range(i):
        x= triple(i)+triple(j)
        x=cube_root(x)
        if x.is_integer() and i > 0 and j>0:
            print(i,j)
            break
print(cube_root(triple(12)+1))
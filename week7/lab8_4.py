

def insertion(list_in,sorted=None):
    if len(list_in) == 0:
        return sorted
    if sorted == None:
        sorted = [list_in.pop(0)]
    if len(list_in) > 0:
        data = list_in.pop(0)
        sorted = insertion_sort(sorted,data).copy()

    return insertion(list_in,sorted)
    

def insertion_sort(sorted:list,data,index = 0):
    
    if index+1 >= len(sorted):
        if data > sorted[0]:
            sorted.insert(index+1,data)

            return sorted
        else:

            sorted.insert(index,data)
            return sorted
    if data > sorted[index] and data <= sorted[index+1]:
        sorted.insert(index+1,data)
        return sorted
    if data < sorted[index]:
        sorted.insert(index,data)
        return sorted
    elif data > sorted[index] and data > sorted[index+1]:
        return insertion_sort(sorted,data,index+1)


alpha = []
for i in range(ord('A'),ord('Z')+1):
    alpha.append(i)
for i in range(ord('a'),ord('z')+1):
    alpha.append(i)

def add_sign_alpha(word:str):
    for i in word:
       
        if is_alpha(i):
            return[ord(i),word]
        
def is_alpha(al):
    global alpha
    return ord(al) in alpha

not_sort = []
index = []
for i in input("Enter Input : ").split(" "):
    # print(i)
    not_sort.append(add_sign_alpha(i))
    index.append(not_sort[-1][0])
    
index = insertion(index).copy()

# print(not_sort)
for i in index:
    for j in range(len(not_sort)):
        if i == not_sort[j][0]:
            print(not_sort[j][1],end=" ")
            not_sort.pop(j)
            break

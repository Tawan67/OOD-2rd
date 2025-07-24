

def min_in_list(list_input):
    min = list_input[0]
    index = 0
    for i in range(len(list_input)):
        if(min>list_input[i]):
            min = list_input[i]
            index = i
    return index

list_a = input().split(' ')
print(list_a)
list_b=[]
for i in list_a:
    list_b.append(int(i))
    
# print(list_b)
# print(max_in_list(list_b))
# print(min_in_list(list_b),end='\n')

sorted_list=[]
for i in range(len(list_b)):
    # index = min_in_list(list_b)
    # print(f"index = {index}, value = {list_b[index]}")
    # list_b.pop(index)
    # print(list_b.pop(min_in_list(list_b)),end=f" {list_b}\n")
    sorted_list.append(list_b.pop(min_in_list(list_b)))

print(sorted_list)
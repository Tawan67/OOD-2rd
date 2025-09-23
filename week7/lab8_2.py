def sort_except_negative(array:list):
    nega_index = []
    nega_value = []
    positive = []
    max_index = len(array)
    for i in range(len(array)):
        if array[i] < 0:
            nega_index.append(i)
            nega_value.append(array[i])
        else:
            positive.append(array[i])
      
        
    # print(nega_index)
    # print(nega_value)
    positive = bubble_sort(positive).copy()
    new_array = []
    
 
    for i in range(max_index):
        if len(nega_value)>0 and i == nega_index[0]:
            new_array.append(nega_value.pop(0))
            nega_index.pop(0)
        elif len(positive)>0:
            new_array.append(positive.pop(0))
    return new_array

def is_sort(array:list):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            return 0

def bubble_sort(a):
    n = len(a)
    last_index = n - 1
    swaped = True
    while last_index >= 1 and swaped:
        swaped = False
        i = 0
        while i < last_index:
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaped = True
            i += 1
        last_index -= 1
    return a
        
            

def swap(array:list,index_1,index_2):
    temp =array[index_1]
    array[index_1]=array[index_2]
    array[index_2]= temp
    return array

inp = [int(i) for i in input("Enter Input : ").split(" ")]

result = sort_except_negative(inp)
text = ""
for i in result:
    text+=f"{i} "
text = text[:-1]
print(text)
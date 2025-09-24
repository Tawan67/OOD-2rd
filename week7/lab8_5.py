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
        if data[1]['points'] > sorted[-1][1]['points']:
            sorted.insert(index+1,data)

            return sorted
        elif data[1]['points'] == sorted[-1][1]['points']:
            if data[2]['gd'] > sorted[-1][2]['gd']:
                sorted.insert(index+1,data)
                return sorted
            else:
                sorted.insert(index,data)
                return sorted
        else:
            sorted.insert(index,data)
            return sorted
        
    if data[1]['points'] > sorted[index][1]['points'] and data[1]['points'] < sorted[index+1][1]['points']:
        sorted.insert(index+1,data)
        return sorted
    
    if data[1]['points'] >= sorted[index][1]['points'] and data[1]['points'] < sorted[index+1][1]['points']:
        if data[2]['gd'] > sorted[index][2]['gd']:
                sorted.insert(index+1,data)
                return sorted
        else:
                sorted.insert(index,data)
                return sorted
            
    if data[1]['points'] < sorted[index][1]['points']:
        sorted.insert(index,data)
        return sorted
    else:
        return insertion_sort(sorted,data,index+1)
    return sorted




inp = input("Enter Input : ").split("/")
data = []
for i in inp:
    ele = i.split(",")
    name = ele.pop(0)
    total_point = int(ele[0])*3+int(ele[1])*0+int(ele[2])*1
    gd =  int(ele[3])-int(ele[4])
    data.append([name,{"points":total_point},{'gd':gd}])

a = insertion(data)

print('== results ==')
for i in range(len(a)-1,-1,-1):
    print(a[i])

def insertion(list_in,sorted=None):
    if len(list_in) == 0:
        return sorted
    if sorted == None:
        sorted = [list_in.pop(0)]
    if len(list_in) > 0:
        data = list_in.pop(0)
        sorted = insertion_sort(sorted,data).copy()
        
        print(f"{sorted} {list_in}") if list_in else print(f"{sorted}")
    return insertion(list_in,sorted)
    

def insertion_sort(sorted:list,data,index = 0):
    
    if index+1 >= len(sorted):
        if data > sorted[0]:
            sorted.insert(index+1,data)
            print(f"insert {data} at index {index+1} : ",end="")
            return sorted
        else:
            print(f"insert {data} at index {index} : ",end="")
            sorted.insert(index,data)
            return sorted
    if data > sorted[index] and data <= sorted[index+1]:
        sorted.insert(index+1,data)
        print(f"insert {data} at index {index+1} : ",end="")
        return sorted
    if data < sorted[index]:
        sorted.insert(index,data)
        print(f"insert {data} at index {index} : ",end="")
        return sorted
    elif data > sorted[index] and data > sorted[index+1]:
        return insertion_sort(sorted,data,index+1)
    
inp = [int(i) for i in input("Enter Input : ").split(" ")]
result = insertion(inp)
print(f"sorted\n{result}")

def is_sort(array:list):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            return 0
            
    return 1
inp = [int(i) for i in input("Enter Input : ").split(" ")]
if is_sort(inp):
    print("Yes")
else:
    print("No")
def binary_search(li,target):
    post = len(li)-1
    pre = 0
    mid = post//2
    if target < li[pre]:
        return -1
    if target > li[post]:
        return 999
    while mid >= pre and mid <= post:
        if target < li[mid]:
            if target > li[mid - 1]:
                # print(li[mid-1])
              
                return ((target-li[mid-1])/(li[mid]-li[mid-1]))+(mid-1)
            mid-=1
        elif target == li[mid]:
            return mid
        else:
            
            if target > li[mid] and target < li[mid + 1]:
                # print(1,li[mid])
                return (target-li[mid])/(li[mid+1]-li[mid])+(mid)
            mid+=1

inp = input("Enter Input : ").split("/")
target = inp.pop(1)
if '.' in target:
    target = float(target)
else:
    target = int(target)
inp = [float(i) if '.' in i else int(i) for i in inp[0].split()]
index = binary_search(inp,target)
percentile = (index + 1) * 100 /len(inp)
if percentile == 100 or percentile == 0:
    percentile = int(percentile)
print()
if index != -1 and index !=999:
    print(f"index      :   {index:.1f}")
    print(f"percentile :   {percentile}")
elif index == -1:
    print("index      :   -1")
    print("percentile :   0")
else:
    print("index      :   999")
    print("percentile :   100")
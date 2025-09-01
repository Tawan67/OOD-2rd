def search(li,x,low=0,high=-1):
    if high == -1:
        high = len(li)
    if low>high:
        return (-1)
    mid =(low+high)//2
    if li[mid]==x:
        return mid
    elif li[mid] > x:
        return search(li,x,low+1,mid-1)
    return search(li,x,mid+1,high-1)

test = [i for i in range(21) if i%2 == 0]
print(test)
index = search(test,16)
print(index)

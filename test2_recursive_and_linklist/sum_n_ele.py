def sum(li,fromI,toJ,first = 1):
    if toJ > len(li):
        toJ = len(li)-1
    if first:
        fromI-=1
        toJ-=1
        first = 0
    if fromI == 0 :
        return 0
    if fromI == toJ:
        return li[toJ]
    return sum(li,fromI+1,toJ,0)+li[fromI]

def sum2(li,fromI,toJ):
    if toJ > len(li):
        toJ = len(li)-1
    if fromI == 0 :
        return 0
    if fromI == toJ:
        return li[toJ]
    return sum2(li,fromI+1,toJ)+li[fromI]

def sum_init_to_n(li,n):
    if n > len(li):
        n = len(li)
    if n == 0:
        return 0
    elif n==1:
        return li[0]
    else:
        return sum_init_to_n(li,n-1)+li[n-1]
    
li = [i for i in range(10)]
print(li)
a = sum2(li,2,15)
b = sum_init_to_n(li,15)
print(a,b)
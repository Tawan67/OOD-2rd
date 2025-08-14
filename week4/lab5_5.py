def fibo(n):
    if n == 1 or n==2:
        return 1
    return fibo(n-1)+fibo(n-2)

# def make_range(start,end,li=None):
#     if li ==None:
#         li =[]
#     if end <= start:
#         return li
#     li.append(start)
#     return make_range(start+1,end,li)

# def check_plus(result,start,end,i=0, j=0,li = []):
#     if start <= 0 or end <= 0:
#         return li
#     if i >= result:
#         return li
#     if j == end+1:
#         return check_plus(result,start,end,i+1, j=0)
#     a = i+start
#     b = j+start
    
#     if a+b == result:
#         li.append([a,b])
    
#     return check_plus(result,start,end, i, j+1)



i,w = input("Purity and Weight needed: ").split(" ")
i = int(i)
w = int(w)

def purity(n,weight):
    
    if n == 1:
        if weight <= 0:
            return -1
        return weight
    
    ck = fibo(n-1)
    
    start = (weight*2)-ck # minimum a+b can be
    end = start+1 #maximum a+b can be
    a = end//2
    b = end-a
    p_a = purity(n-1,a)
    p_b = purity(n-1,b)
    
    if p_a == -1 or p_b == -1:
        return -1
    stone=p_a+p_b
    
    return stone
print(f"Total weight of used minerals with Purity 1 : {purity(n=i,weight=w)}")
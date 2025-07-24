def pow(base,poww):
    ans = 1
    if poww==0:
        return 1
    for i in range(poww):
        ans = ans*base
    return ans

def dec_to_bi(dec,reverse = 0):
    list_ans=[]
    while dec>1:
        list_ans.append(dec%2)
        dec=dec//2
    list_ans.append(1)
    if(reverse == 1):
        return list_ans
    new_list = []
    # print(list_ans)
    for i in range(len(list_ans)-1, -1, -1):
        new_list.append(list_ans[i])
    return new_list

def bi_to_dec(bi,reverse = 0):
    sum=0
    if reverse==1:
        for i in range(len(bi)):
            
            sum+=(pow(2,i))*bi[i]
            # print(sum ,"+",pow(2,i)*bi[i],i)
    else:
        for i in range(len(bi)-1,-1,-1):
            sum+=(pow(2,(len(bi)-i-1)))*bi[i]
            # print(sum ,"+",pow(2,(len(bi)-i-1)*bi[i]),(len(bi)-i-1))
    if reverse == -1:
        return -sum
    return sum

def Rshift(num,shift):
    list_ans=[]
    if shift==0 and num == 0:
        return 0
    
    negative_num = 0
    if num<0:
        num=-num
        negative_num=1
        
    list_bi=dec_to_bi(num)
    if shift>=0:
        for i in range(len(list_bi)-shift):
            list_ans.append(list_bi[i])
    else:
        list_ans.clear
        list_ans.extend(list_bi)
        for i in range(-shift):
            
            list_ans.append(0)
    # return list_ans
    if negative_num==1:
        return bi_to_dec(list_ans,-1)

    return bi_to_dec(list_ans)
    pass
    ### Enter Your Code Here ###

n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))


# dec_cal = bi_to_dec(list_bi,1)
# print(list_bi,dec_cal)

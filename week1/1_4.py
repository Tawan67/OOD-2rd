def odd_list(al):
    ans=[]
    for i in al:
        if i%2==1:
            ans.append(i)
    return ans
    # เติมส่วนของคำสั่ง
    pass


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]

opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)

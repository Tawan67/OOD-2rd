def luck_number(num):
    if num<10:
        return num
    lsd = num%10 #LSD IS  Least significant digits
    return lsd + luck_number(num//10)
def til_zero(num,count = 1):
    if num >=10:
        num = luck_number(num)
        if num > 9:
            print("Sum #%d : %d"%(count,num))
            count+=1
        return til_zero(num,count) 
    elif num < 10:
        print(f"Lucky Number: {num}")
        return 0
    
    

num = input("Enter Input: ")
num = int(num)
til_zero(num)
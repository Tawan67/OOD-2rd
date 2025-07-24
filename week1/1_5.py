num=int(input("Enter Input : "))
for i in range(num+2):
    for j in range(num+2):
        if (num+1-i)>j:
            print(".",end="")
        else:
            print("#",end='') 
    for j in range(num+2):
        if j==0 or i==0 or j==num+1 or i==num+1:
            print("+",end="")
        else:
            print("#",end='')
    print()
for i in range(num+2):
    for j in range(num+2):
        if j==0 or i==0 or j==num+1 or i==num+1:
            print("#",end="")
        else:
            print("+",end='')
    for j in range(num+2):
        if (num+2-i)>j:
            print("+",end="")
        else:
            print(".",end='') 
    print()
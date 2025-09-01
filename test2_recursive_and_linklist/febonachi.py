def febo(n):
    if n ==0:
        return "Error"
    if n ==1 or n==2:
        return 1
    return febo(n-1)+ febo(n-2)
# inp =int(input("input you series of febo : "))
# a = febo(inp)
# print(a)
for i in range(20):
    print(f"febo {i} is ",febo(i))
    
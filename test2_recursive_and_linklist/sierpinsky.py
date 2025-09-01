def sier(n):
    if n ==1:
        return 5
    return 2 + (3*sier(n-1))
n = int(input("input your floor"))
print(sier(n))
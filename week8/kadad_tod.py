inp = input("data: ").split(" ")
key = 0
for i in inp[0]:
    key+=ord(i)
print(key%int(inp[1]))
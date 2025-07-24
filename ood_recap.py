# from week2_stack_and_queue.stack import Stack
# a ='a'
# print(chr(ord(a)+1))
# b =Stack()
# print(b.pop_item)
# num = [str(i) for i in range(10)]
# print(num)

def formating(equa):
    sum=""
    new_equa=[]
    for i in equa:
        if i.isnumeric():
            sum+=i
        else:
            if sum != '':new_equa.append(sum)
            new_equa.append(i)
            sum = ''
    new_equa.append(sum)
    return new_equa
equa = input("KoLo: ")
print(formating(equa))
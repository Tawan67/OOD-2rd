from stack import Stack

def formating(equa):
    sum=""
    new_equa=[]
    for i in equa:
        if i.isnumeric() or i =='.':
            sum+=i
        else:
            if sum != '':new_equa.append(sum)
            new_equa.append(i)
            sum = ''
    new_equa.append(sum)
    new_equa = [i for i in new_equa if i != '']
    return new_equa

def is_float(element):
    if not("." in element):
        return 0
    for i in element:
        if i == '.':
            initial  = element.index(i)
            try:
                if not(element[initial-1].isnumeric() and element[initial+1].isnumeric()):
                    return 0
            except:
                return 0
    return 1

def check_equa(equa):
    equa = [i for i in equa if i != " "]
    if len(equa)<=1:
        return 0
    open=Stack()
    num = [str(j) for j in range(10)]
    open_text = ['(','{','[']
    close_text = [')','}',']']
    operation = ['+','-','*','/']
    num = num +open_text+close_text
    all = num+operation+['.']
    
    for i in equa:
        if i in open_text:
            open.push(i)
        if i in close_text:
            if not(close_text.index(i) == open_text.index(open.pop_item)):
                return 0
        if not(i in all):return 0
    for i in range(len(equa)):
        if equa[i] in operation:
            if i == len(equa)-1 or i == 0:
                return 0
            if not(equa[i-1] in num and equa[i+1] in num):
                return 0
    return 1

def postfix_form(equation):
    equa = [i for i in equation if i != " "]
    if not check_equa(equa):
        return "Invalid Equation"
    equa=formating(equa)
    equa+="."
    number = [str(i) for i in range(10)]
    oper_1 = ['+','-']
    oper_2 = ['*','/']
    open_text = ['(','{','[']
    close_text = [')','}',']']
    custom_order = {}
    custom_order_inside = custom_order.copy
    for i in number:
        custom_order[i]=0
    for i in oper_1:
        custom_order[i]=1
    for i in oper_2:
        custom_order[i]=2
    for i in open_text:
        custom_order[i]=3
    for i in close_text:
        custom_order[i]=4
    custom_order_inside = custom_order.copy()
    for i in open_text:
        custom_order_inside[i]=0
    num = Stack()
    oper = Stack()
    anwser = list()
    buffer = custom_order.copy()
    for i in equa:
        if i.isnumeric() or is_float(i):
            if num.isEmpty:
                num.push(i)
            else:
                anwser.append(num.pop_item)
                num.push(i)
        else:
            if oper.isEmpty and i!='.' and not(i in open_text): #case first operation except open text
                oper.push(i)
                anwser.append(num.pop_item)
                
            elif  i !='.' and not(oper.isEmpty) and not(i in close_text) and  custom_order[oper.peek] < custom_order[i] and not(i in open_text): # * to + not open text
                anwser.append(num.pop_item)
                oper.push(i)
                
            elif  i !='.' and not(oper.isEmpty) and not(i in close_text) and custom_order[oper.peek] > custom_order[i] and not(i in open_text): # + to * pop-->num,oper,oper...
                anwser.append(num.pop_item)
                if not (oper.peek in open_text) :anwser.append(oper.pop_item)
                while not(oper.isEmpty) and not(oper.peek in open_text):anwser.append(oper.pop_item)
                oper.push(i)
            elif i in open_text:
                oper.push(i)
                custom_order=custom_order_inside.copy()
            elif i in close_text:
                anwser.append(num.pop_item)
                if not(oper.peek in open_text):anwser.append(oper.pop_item)
                while not(oper.isEmpty) and not (oper.peek in open_text) :
                    anwser.append(oper.pop_item)
                if not(oper.isEmpty) and oper.peek in open_text:
                    oper.pop_item
                custom_order = buffer.copy()
            elif i !='.' and custom_order[oper.peek] == custom_order[i]: # + เจอ +
                anwser.append(num.pop_item)
                anwser.append(oper.pop_item)
                if i!= '.':oper.push(i)
            elif  i =='.':
                    anwser.append(num.pop_item)
                    anwser.append(oper.pop_item)
                    while not oper.isEmpty:
                        if oper.peek in open_text or oper.peek in close_text:
                            oper.pop_item
                        if not(oper.isEmpty):anwser.append(oper.pop_item)
            
            # if oper.isEmpty and i !='.': # operation ว่าง
            #     oper.push(i)
            # elif i !='.' and custom_order[oper.peek] < custom_order[i] and not (oper.peek in open_text): # * ทับ + == เอา เลข ออก เก็บ บวก  
            #     anwser.append(num.pop_item)
            #     oper.push(i)
            #     # print(oper)
            # elif i in open_text and not (oper.peek in open_text) :
            #     anwser.append(num.pop_item)
            #     anwser.append(oper.pop_item)
            #     while (not oper.peek in open_text) and not (oper.isEmpty):
            #         anwser.append(oper.pop_item)
            #     pass
            # elif i !='.' and custom_order[oper.peek] > custom_order[i]:# + ทับ * == เอา เงข ออก * ออก ก่อน * ออก แล้ว add +
            #     anwser.append(num.pop_item)
            #     anwser.append(oper.pop_item)
            #     if not oper.isEmpty: anwser.append(oper.pop_item)
            #     if i!= '.':oper.push(i)
        
            # elif i !='.' and custom_order[oper.peek] == custom_order[i]: # + เจอ +
            #     anwser.append(num.pop_item)
            #     anwser.append(oper.pop_item)
            #     if i!= '.':oper.push(i)
            # elif i =='.' :
            #     anwser.append(num.pop_item)
            #     anwser.append(oper.pop_item)
            #     while not oper.isEmpty:
            #         anwser.append(oper.pop_item)
            anwser = [i for i in anwser if i!= None]
    return anwser

def cal(equa:list):
    num_stack = Stack()
    if equa =="Invalid Equation":
        return equa
    
    for i in equa:
        if i.isnumeric() or is_float(i):
            if is_float(i):
                num_stack.push(float(i))
            else:
                num_stack.push(int(i))
        else:
            print(num_stack)
            b = num_stack.pop_item
            a = num_stack.pop_item
            if i =='+':
                num_stack.push(a+b)
            if i =='-':
                num_stack.push(a-b)
            if i =='*':
                num_stack.push(a*b)
            if i =='/':
                num_stack.push(a/b)
    return num_stack.pop_item
        
      

equa = input("Input Your Eqution :")
result = postfix_form(equa)
print(result)
print(cal(result))
print((12.90-12)*10/3+12)

def search(li:list,data):
    for i in range(len(li)):
        if data == li[i]:
            li.insert(0,li.pop(i))
            return i+1,li
    return -1,li
def heuristic(li:list,data):
    index,new_li = search(li,data)
    text = ''
    for i in new_li:
        text += i+" "
    if index > -1:
        print(f"Search {data} -> found at {index} move to front ->  {text}")
        return index,data,0
    else:
        print(f"Search {data} -> not found -> {text}")
        return len(li)+1,data,1
def main():
    print("This is your BOOK!!!")
    inp,borrow = input("Enter input: ").split("/")
    inp = inp.split(" ")
    borrow = borrow.split(" ")
    shelt = []
    cost = 0
    for target in borrow:
        if target in shelt:
            cost+=1
            newbook = shelt.pop(shelt.index(target))
            inp.insert(0,newbook)
            text = ''
            for i in inp:
                text += i+" "
            print(f"Search {newbook} -> add new book ->  {text}")
            continue
        borrow_price,book,new = heuristic(inp,target)
        if new:
            shelt.append(book)
        cost+=borrow_price
        
    text = ''
    for i in inp:
        text += i+" "
    print()
    print(f"Final books: {text}")
    print(f"Total cost: {cost}")

main()
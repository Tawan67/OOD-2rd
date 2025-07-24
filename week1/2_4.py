def hbd(year):
    if not isinstance(year,int):
        year = int(year)
        
    base = year//2
    if base*2 == year:
       
        return f"saimai is just {20}, in base {base}!"
    else:
        
        return f"saimai is just {21}, in base {base}!"

    ### Enter Your Code Here ###

year = input("Enter year : ")

print(hbd(int(year)))
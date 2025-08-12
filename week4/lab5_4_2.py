def flood_fill(map, r, c, current_h):
    R = len(map)
    C = len(map[0])
    
    if r < 0 or r >= R or c < 0 or c >= C:
        return
    
    if map[r][c] > current_h:
        return

    if map[r][c] == 0:
        return

    past_h = map[r][c]

    map[r][c] = 0

    flood_fill(map, r-1, c, past_h)  # on
    flood_fill(map, r+1, c, past_h)  # under
    flood_fill(map, r, c-1, past_h)  # left
    flood_fill(map, r, c+1, past_h)  # right


        
def main():
    print(" *** Water Flow ***")
    
    inp = input("Input rows,cols/data1,data2,.../start_row,start_col : ").split("/")
    R,C = inp.pop(0).split(",")
    R = int(R)
    C = int(C)
    if R > 9 or R<1 or C> 9 or C<1:
        print("Error: Rows and columns must be between 1 and 9")
        return
    x,y = inp.pop(-1).split(",")
    x = int(x)
    y = int(y)
    temp = []
    map = []
    row = inp[0].split(",")
    
    for i in row:
        temp = []
        for j in i:
            temp.append(int(j))
        map.append(temp)
    
    try:
        a = map[x][y]
    except:
        print("Error: Start coordinates are out of grid bounds")
        return    
    
    flood_fill(map,x,y,map[x][y])
    for row in map:
        r = [str(i) for i in row]
        print("".join(r))
main()



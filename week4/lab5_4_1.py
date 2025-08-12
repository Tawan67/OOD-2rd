def Relu(n):
    if n < 0:
        return 0
    return n


def rc_map(map,point):
    r,c = point.split(",")
    r = int(r)
    c = int(c)
    h = len(map)-1
    w = len(map[0])-1
    position = is_kob(c,r,w,h)
    
    on  = position[0]
    under  = position[1]
    left  = position[2]
    right  = position[3]
    
    if on != 0:
        if map[on[0]][on[1]]>map[r][c] and map[on[0]][on[1]] != 0:
            on =  0
        else:
            on = rc_map(map,f"{on[0]},{on[1]}")
    if under != 0:
        if map[under[0]][under[1]]>map[r][c] and map[under[0]][under[1]] != 0:
            under = 0
        else:
            under = rc_map(map,f"{under[0]},{under[1]}")
    if left != 0:
        if map[left[0]][left[1]]>map[r][c] and map[left[0]][left[1]] != 0:
            left = 0
        else:
            left = rc_map(map,f"{left[0]},{left[1]}")
    if right != 0:
        if map[right[0]][right[1]]>map[r][c] and map[right[0]][right[1]] != 0:
            right = 0
        else:
            right = rc_map(map,f"{right[0]},{right[1]}")
    
    if on == 0 and under == 0 and left == 0 and right == 0:
        map[r][c]=0
    return map[r][c]
    
    # if isinstance(on,list):
    #     o = int(not(map[r][c] >= map[on[1]][on[0]]))
    # else:
    #     o = 0
    # if isinstance(under,list):
    #     u = int(not(map[r][c] >= map[under[1]][under[0]]))
    # else:
    #     u = 0
    # if isinstance(left,list):
    #     l = int(not(map[r][c] >= map[left[1]][left[0]]))
    # else:
    #     l = 0
    # if isinstance(right,list):
    #     r = int(not(map[r][c] >= map[right[1]][right[0]]))
    # else:
    #     r = 0
    
    # if o+u+l+r == 0:
    #     return 0
    
    # return 
    
def is_kob(x,y,w,h): #y == row , x == col
    if x == 0 and y == 0: #left on
        position = [0,[y+1,x],0,[y,x+1]]  # on under left right
        return position
    elif x == w and y == 0: #right on
        position =[0,[y+1,x],[y,x-1],0]
        return position
    elif x == 0 and y == h: #left down
        position =[[y-1,x],0,0,[y,x+1]]
        return position
    elif x == w and y == h: #right down
        position =[[y-1,x],0,[y,x-1],0]
        return position
    elif y == 0:
        position =[0,[y+1,x],[y,x-1],[y,x+1]]
        return position
    elif y == h:
        position =[[y-1,x],0,[y,x-1],[y,x+1]]
        return position
    elif x == 0:
        position =[[y-1,x],[y+1,x],0,[y,x+1]]
        return position
    elif x == w:
        position =[[y-1,x],[y+1,x],[y,x-1],0]
        return position
    else:
        position =[[y-1,x],[y+1,x],[y,x-1],[y,x+1]]
        return position



s = [[1,2,3,4],
     [1,2,2,2],
     [1,2,2,3],
     [4,4,4,4]]
# a= is_kob(1,1,3,3)
rc_map(s,"1,1")
print(s)

# print(a)
# print(s[1][1])
# for i in range(len(a)):
#     print(f"{i} =",s[a[i][0]][a[i][1]])
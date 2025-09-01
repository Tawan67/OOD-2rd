def n_queen(n):
    board = n*[-1]
    colFree = n*[1]
    upFree = (2*n - 1) * [1]
    downFree = (2*n - 1) * [1]
    return put_queen(0,board,colFree,upFree,downFree)

numSol = 0

def put_queen(r,board,colFree,upFree,downFree):
    global numSol
    for c in range(len(board)):
        if colFree[c] and upFree[r+c] and downFree[r-c+(len(board))-1]:
            board[r] = c
            colFree[c] = upFree[r+c] = downFree[r-c+(len(board))-1] = 0
            if r == len(board) - 1:
                print(board)
                numSol+=1
            else:
                put_queen(r+1,board,colFree,upFree,downFree)
        colFree[c] = upFree[r+c] = downFree[r-c+(len(board))-1] = 1
        
n_queen(4)
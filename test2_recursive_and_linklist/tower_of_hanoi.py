
def move(n,A,C,B):
    if n == 1:
        print(f"{n} from {A} to {C}") #base a is 1
    else:
        move(n-1,A,B,C) #move n-1 from a to b then a are 1,2,3 and b is 4 1recursive case
        print(f"{n} from {A} to {C}")
        move(n-1,B,C,A) #move B to C
        
move(4,'A','C','B')
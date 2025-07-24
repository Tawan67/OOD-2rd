class Stack:
    """class stack
    create empty stack"""
    total = 0
    def __init__(self):
        self.items =[]
        self.size = 0
        Stack.total += 1

s =Stack()
print(s.items)
print(s.size)
s2=Stack()
print(s.total)
stack =[]
def push():
    ele = int(input("Enter Element: "))
    stack.append(ele)

def pop():
    if len(stack) is None:
        print("Underflow ! stack is empty")
    stack.pop()

def peek():
    if len(stack) == 0:
        print("Stack is Empty")
    print(stack[-1])

def display():
    print(stack)

def size():
    print(len(stack))
    
print("__STACK OPERATIONS__")
print("1-->PUSH / 2-->POP / 3-->PEEK / 4-->DISPLAY LIST / 5--> SIZE / 6-->EXIT ")
while True:
    oper = int(input("Operation: "))
    if oper == 1:
        push()
    elif oper == 2:
        pop()
    elif oper ==3:
        peek()
    elif oper == 4:
        display()
    elif oper ==5:
        size()
    elif oper == 6:
        print("Exit")
        break
    else:
        print("Invalid Integer")




        

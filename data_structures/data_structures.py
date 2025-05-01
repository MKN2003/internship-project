stack = []
queue = []

# Stack operations
def push(item):
    stack.append(item)
    return print(f"Stack: {stack}")
    

def pop():
    if stack:
        stack.pop()
        return print(f"Stack: {stack}")
    return print('Stack is empty. Add element first')


# Queue operations
def enqueue(item):
    queue.append(item)
    return print(f"Queue: {queue}")

def dequeue():
    if queue:
        queue.pop(0)
        return print(f"Queue: {queue}")
    return print('Queue is empty. Add element first')

while True:
    menu = int(input("1. Stack\n"
                     "2. Queue\n"
                     "0. Exit\n"
                     "Input: "))
    if menu == 1:
        while True:
            menu_stack = int(input("1.Add element to the stack\n"
                                   "2. Delete element from the stack\n"
                                   "0.Exit\n"
                                   "Input: "))
        
            if menu_stack == 1:
                push(item=input("Add something to for the stack: "))
            if menu_stack == 2: 
                pop()
            if menu_stack == 0: 
                break
    if menu == 2:
        while True:
            menu_stack = int(input("1.Add element to the queue\n"
                                   "2.Delete element from the queue\n"
                                   "0.Exit\n"
                                   "Input: "))
            if menu_stack == 1:
                enqueue(item=input("Add something to for the queue: "))
            if menu_stack == 2: 
                dequeue()
            if menu_stack == 0: 
                break
    if menu == 0:
        break
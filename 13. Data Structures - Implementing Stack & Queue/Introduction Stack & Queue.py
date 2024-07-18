## Introduction To Stack as a List
# A stack is a LIFO (Last In, First Out) data structure. This means the last element you insert is the first one you take out.

# Push (Add to top of stack)
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
print(numbers) #"Stack after pushes:"

# Pop (Remove top of stack)
print(numbers.pop()) #"Popped element:"

# Top (Inspect top of stack)
print(numbers[-1]) #"Top of stack:"

# IsEmpty (Check if stack is empty)
print(not bool(numbers)) #"Is stack empty?"

## Implementing Stack
# Stacks can be used to implement undo functionality in applications.

# START BUILDING A STACK
# Step 1: Initialize Stack Class
class Stack:
    def __init__(self):
        self.items = [] 

# Step 2: Push Element
    def push(self, item):
        self.items.append(item)

# Step 3: Check if Stack is Empty
    def is_empty(self):
        return len(self.items) == 0
    
# Step 4: Pop Element
    def pop(self):
        if not self.is_empty():  
            return self.items.pop()
        
# Step 5: Top Element
    def top(self):
        if not self.is_empty():  
            return self.items[-1] 
        
# Step 6: Display the Stack
    def display(self):
        print(self.items)

# Create a Stack
s = Stack()
 
# Push elements
s.push(1)  
s.push(2)  
s.push(3)  
 
# Display the stack
s.display()  
 
# Pop elements
print(s.pop())  
s.display()  
 
# Top element
print(s.top())  
 
# Check if stack is empty
print(s.is_empty())        

## Introduction to Queue as a List
# A queue follows a FIFO (First In, First Out) principle.

# Enqueue (Add to rear of queue)
numbers = []
 
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
 
print(numbers)  #"Queue after enqueues:"

# Dequeue (Remove front of queue)
print(numbers.pop(0)) #"Dequeued element:"

# Front (Inspect front of queue)
print(numbers[0]) #"Front of queue:"

# IsEmpty (Check if queue is empty)
print(not bool(numbers)) #"Is queue empty?"

## Implementing Queue
# Stacks can be used to implement undo functionality in applications.

# START BUILDING A STACK
# Step 1: Initialize Queue Class
class Queue:
    def __init__(self):
        self.items = [] 

# Step 2: Enqueu Element
    def enqueue(self, item):
        self.items.append(item)

# Step 3: Check if Queue is Empty
    def is_empty(self):
        return len(self.items) == 0
    
# Step 4: Dequeue Element
    def dequeue(self):
        if not self.is_empty():  
            return self.items.pop(0)
        
# Step 5: Front Element
    def front(self):
        if not self.is_empty():  
            return self.items[-1] 
        
# Step 6: Display the Queue
    def display(self):
        print(self.items)

# Create a Queue
q = Queue()
 
# Enqueue elements
q.enqueue(1) 
q.enqueue(2)
q.enqueue(3)
 
# Display the queue
q.display()  
 
# Dequeue elements
print(q.dequeue())  
q.display()  
 
# Front element
print(q.front())  
 
# Check if queue is empty
print(q.is_empty())        
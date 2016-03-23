

#2) Design a stack which, in addition to push and pop, has a function min which 
# returns the minimum element in the stack.

class StackWithMin: 
    def __init__(self): 
        self.stack = []
        self.min = [float("inf")]

    def get_min(self): 
        if self.min[-1] == float("inf"): 
            return "No Min"
        else: 
            return sef.min[-1]

    def push(self, value): 
        if value < self.min[-1]: 
            self.min.append(value)
        self.stack.append(value)

    def pop(self): 
        value = self.stack.pop()
        if value == self.min[-1]: 
            self.min.pop()
        return value

# test = StackWithMin()
# [test.push(x) for x in '174836423']

#***************************************************************************************
#3) Implement a data structure SetOfStacks() that starts a new stack when the previous stack
# exceeds some threshold

class SetOfStacks: 
    def __init__(self, size=100): 
        self.capacity = size
        self.current_stack = []
        self.filled_stacks = []


    def push(self, value): 
        if len(self.current_stack) < self.capacity: 
            self.current_stack.append(value)
        else: 
            old_stack = list(self.current_stack)
            self.filled_stacks.append(old_stack)
            self.current_stack = [value]

    def SetPop(self): 
        if len(self.current_stack) == 0 and not self.filled_stacks: 
            return "Empty Stack"
        elif len(self.current_stack) == 0: 
            self.current_stack = self.filled_stacks.pop()
        return self.current_stack.pop()

# my_stack = SetOfStacks(10)
# [my_stack.push(x) for x in range(1, 10)]

#****************************************************************************************
#4) Implement MyQueue class which implements a queue using two stacks


class MyQueue(object):
    """
    Implements a queue using two stacks.
    Lazily reverses items from the back_stack to the front_stack when needed.
    """
    def __init__(self):
        self.front_stack = Stack()
        self.back_stack = Stack()

    def eq(self, data):
        self.back_stack.push(data)

    def dq(self):
        if self.front_stack.size == 0:
            self.rebuild()
        return self.front_stack.pop()

    def peek_front(self):
        if self.front_stack.size == 0:
            self.rebuild()
        return self.front_stack.peek()
    
    def rebuild(self):
        """
        Lazily rebuilds the front stack when a value is needed by pop/peek.
        When the front_stack empties, rebuild it by reversing the values in
        the back_stack.
        """
        while self.back_stack.size > 0:
            self.front_stack.push(self.back_stack.pop())



### NODE AND STACK IMPLEMENTATION  ###
from copy import deepcopy
class Node(object):
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return str(self.data)
        

# class Stack(object):
#     def __init__(self):
#         self.stack = Node()
#         self.size = 0

#     def push(self, data):
#         self.stack = Node(data, self.stack)
#         self.size += 1

#     def pop(self):
#         assert self.stack.data is not None, 'Stack is empty'
#         value = self.stack.data
#         self.stack.data = self.stack.nextNode.data
#         self.stack.nextNode = self.stack.nextNode.nextNode
#         self.size -= 1
#         return value
    
#     def peek(self):
#         assert self.size > 0, 'Stack is empty'
#         return self.stack.data

#     def __str__(self):
#         stack_copy = deepcopy(self)
#         tempHolder = []
#         while stack_copy.size > 0:
#             tempHolder.append(stack_copy.pop())
#         return ', '.join(map(str, tempHolder[::-1]))

#****************************************************************************************
#5) Write a program to sort a stack such that the smallest items are on the top. You can use a 
# temporary stack. 

class Stack(list):
    def peak(self):
        return self[-1]
    def push(self, item):
        self.append(item)
    def empty(self):
        return len(self) == 0



def sort_stack(s):
    r = Stack()
    while not s.empty():            
        tmp = s.pop()
        while not r.empty() and r.peak() > tmp:
            s.push(r.pop())
        r.push(tmp)
        while not s.empty() and s.peak() >= r.peak():
            #warning, >= here
            r.push(s.pop())
    return r

from random import randrange
test_items = [randrange(20) for x in xrange(20)]
print test_items
S = Stack()
for item in test_items:
    S.push(item)
# S = sort_stack(S)
print S
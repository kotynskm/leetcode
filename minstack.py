""" Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function. """

class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

# O(1) min stack
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        # push val onto stack
        self.stack.append(val)
        # if items in the minStack, get the min between val and min in stack, else get the min between val and val if minStack is empty
        if self.minStack:
            val = min(self.minStack[-1], val)
        else:
            val = min(val, val)
            
        self.minStack.append(val)

    def pop(self) -> None:
        # pop item off both stack and minStack
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # return last item in stack
        return self.stack[-1]

    def getMin(self) -> int:
        # return last item in the minStack
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
""" Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise. """

class MyQueue:

    def __init__(self):
        self.elements = []

    def push(self, x: int) -> None:
        return self.elements.append(x)

    def pop(self) -> int:
        return self.elements.pop(0)

    def peek(self) -> int:
        return self.elements[0]

    def empty(self) -> bool:
        return len(self.elements) == 0

# this is implementation of a queue using 2 stacks
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # if items already in s1, we must move the items over to s2
        while self.s1:
            self.s2.append(self.s1.pop())
        # then append the item to s1
        self.s1.append(x)
        
        # now move the items back over to s1 from s2 (the items that would have been first in the queue)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()
        
    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
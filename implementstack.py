""" Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty). """

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        # while we have items in front, we want to pop them off and push them to the back of the q (all except the last one)
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        # now return the last item
        return self.q.popleft()
        
    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
""" Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream. """

class MovingAverage:

    def __init__(self, size: int):
        self.window = size
        self.q = deque()
        
    def next(self, val: int) -> float:
        # add vals to q and calc avg based on number of items in the q
        # if q size reaches window size, then popleft and add the next val
        # return avg of the numbers inside q
        length = len(self.q)
        if length == self.window:
            self.q.popleft()
            self.q.append(val)
        else:
            self.q.append(val)

        return sum(self.q)/len(self.q)
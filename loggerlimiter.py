"""Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false."""

class Logger:

    def __init__(self):
        self.map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # if message is not in the map, add it with the timestamp
        if message not in self.map:
            self.map[message] = timestamp
            return True
        # if it's already in the map, check if current timestamp - the stored timestamp is >= 10
        if timestamp - self.map.get(message, 0) >= 10:
            self.map[message] = timestamp
            return True
        
        return False

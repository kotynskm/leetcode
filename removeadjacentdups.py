""" You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique."""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        # use a stack
        stack = []
        
        # if letter is same as last in stack, pop it off
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            # if not, add it to the stack
            else:
                stack.append(char)
        
        
        return "".join(stack)
    
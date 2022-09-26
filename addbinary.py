""" Given two binary strings a and b, return their sum as a binary string. """

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return value is a str 
        result = ""
        # keep track of carry value
        carry = 0
        
        # turn into list and use pop to get values
        a = list(a)
        b = list(b)
        
        while a or b or carry == 1:
            # if we have values, remove the last item and cast to int and add to carry
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
                
            # add the value of carry to result, use mod to get remainder because we only use 0 and 1 values and cast back to str
            result += str(carry % 2)
            # update carry
            carry = carry // 2
        
        return result[::-1]
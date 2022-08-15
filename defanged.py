""" Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]". """

# using replace method
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

# using loop and result string
class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        
        for c in address:
            if c == ".":
                result += "[.]"
            else:
                result += c
                
        return result

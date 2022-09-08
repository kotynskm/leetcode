""" Given two strings s and t, return true if they are equal when both are typed into empty text editors. 

'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty. """

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # create helper function that builds result string using a stack
        def buildStr(s):
            result = []
            
            # iterate str and use result as a stack
            for c in s:
                if c != "#":
                    result.append(c)
                else:
                    if result:
                        result.pop()
            # convert back to string
            return "".join(result)
        
        return buildStr(s) == buildStr(t)
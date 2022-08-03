""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""
def isValid(s):
    # use a hash map to store value of parens
    # use a stack to keep track of parens
    
    parens_dict = { ")":"(", "]":"[", "}": "{" }

    stack = []

    for char in s:
        # check if char is a closed parens
        if char in parens_dict:
            # if it is, check that we have items in our stack AND the top item 
            # is a matching open parens
            if stack and stack[-1] == parens_dict[char]:
                stack.pop()
                # we have no opening parens in our stack to match the closed parens
            else:
                return False

        # it is an open parens
        else:
            stack.append(char)

        return not stack


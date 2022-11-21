""" You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

 """

 class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # loop over number and check for digit
        # if we find the digit, splice it out
        # add the splice to an output array
        # return the max of the output array
        output = []

        for i in range(len(number)):
            if number[i] == digit:
                output.append(number[:i] + number[i + 1:])

        return max(output)
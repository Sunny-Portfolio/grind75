import re


class Solution:

    # Solution 1 - Use String method to replace brackets
    def isValid(self, s: str) -> bool:

        for i in range(len(s)):
            s = s.replace("()", "")
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        return not s

    # Solution 2 - Use regex
    def isValid2(self, s: str) -> bool:
        while True:
            og = s
            s = re.sub(r'\(\)', '', s)
            s = re.sub(r'\[\]', '', s)
            s = re.sub(r'\{\}', '', s)

            # if no replacement match found, break loop
            if og == s:
                break
        return not s

    # Solution 3 - Use stack
    def isValid3(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in '([{':
                stack.append(x)     # add to stack
            else:   # check matching close bracket and pop
                if not stack or \
                        stack[-1] == '(' and x != ')' or \
                        stack[-1] == '[' and x != ']' or \
                        stack[-1] == '{' and x != '}':
                    return False
                stack.pop()

        return not stack


xx = "{{[()]}}"
print(Solution().isValid(xx))
print(Solution().isValid2(xx))
print(Solution().isValid3(xx))

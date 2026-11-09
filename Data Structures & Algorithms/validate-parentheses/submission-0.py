class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in close_to_open:
                top = stack.pop() if stack else '#'
                if close_to_open[c] != top:
                    return False
            else:
                stack.append(c)
        return not stack
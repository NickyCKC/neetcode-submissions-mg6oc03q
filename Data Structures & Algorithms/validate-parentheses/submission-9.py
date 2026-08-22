from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque([])
        for c in s:
            if c == "(":
                queue.append(")")

            elif c == "[":
                queue.append("]")

            elif c == "{":
                queue.append("}")
            
            else:
                if queue and queue[-1] == c:
                    queue.pop()
                else:
                    return False
      
        return True if not queue else False
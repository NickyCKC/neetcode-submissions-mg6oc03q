class Solution:
    def countSubstrings(self, s: str) -> int:
        resLen = 0
        resIdx = 0
        counter = 0

        for i in range(len(s)):
            l, r = i, i
            while s[l] == s[r]:
                counter += 1
                if l - 1 < 0 or r + 1 >= len(s):
                    break
                l -= 1
                r += 1
        
        for i in range(len(s)):
            l = i
            if i + 1 >= len(s):
                break
            r = i + 1
            while s[l] == s[r]:
                counter += 1
                if l - 1 < 0 or r + 1 >= len(s):
                    break
                l -= 1
                r += 1
        
        return counter
                

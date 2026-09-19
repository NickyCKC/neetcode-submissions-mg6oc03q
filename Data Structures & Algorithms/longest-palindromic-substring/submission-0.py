class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resIdx = 0

        for i, c in enumerate(s):
            l = i
            r = i
            while s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    resIdx = l
                if l - 1 < 0 or r + 1 >= len(s):
                    break
                l -= 1
                r += 1

            l = i
            if i + 1 >= len(s):
                continue
            r = i + 1
            while s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    resIdx = l
                if l - 1 < 0 or r + 1 >= len(s):
                    break
                l -= 1
                r += 1

        return s[resIdx: resIdx + resLen]

        
        

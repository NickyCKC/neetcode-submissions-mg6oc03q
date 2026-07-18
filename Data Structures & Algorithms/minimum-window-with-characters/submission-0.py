class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        
        countT = {}
        for ltr in t:
            countT[ltr] = 1 + countT.get(ltr, 0)
        
        window = {}
        have = 0
        need = len(countT)
        res = [-1, -1]
        reslen = float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if reslen != float("infinity") else ""
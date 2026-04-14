class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        dictf = {}
        longest = 0

        for r in range(len(s)):
            if s[r] in dictf:
                dictf[s[r]] += 1
                #dictf[s[r]] = 1 + dictf.get(s[r], 0)
            else:
                dictf[s[r]] = 1
            maxf = max(maxf, dictf[s[r]])
            while (r - l + 1) - maxf > k:
                dictf[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest


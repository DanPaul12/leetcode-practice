class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_word= []
        l = 0
        r = 1
        count = 1

        if not s:
            return 0

        while r < len(s):
            unique_word.append(s[l])
            if s[r] in unique_word:
                l += 1
                r += 1
            while r < len(s) and s[r] not in unique_word:
                unique_word.append(s[r])
                count = max(count, len(unique_word))
                r += 1
            l += 1
            r = l + 1
            unique_word = []
        return count
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        seen = set()
        left = 0
        for c in s:
            while c in seen:
                seen.remove(s[left])
                left += 1

            seen.add(c)
            maxLength = max(maxLength, len(seen))

        return maxLength
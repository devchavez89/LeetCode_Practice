# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

#Use a HashMap and update the indexes to record the longest substring

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStrMap = {}
        maxSubLength = 0
        curSubLength = 0
        length = 0
        i = 0

        while i < len(s):
            # If value is in dict and index of char is > current substring length
            if s[i] in subStrMap and subStrMap[s[i]] >= curSubLength:
                # Set sub string to start after duplicate first found, ex. index 1(b)
                curSubLength = subStrMap[s[i]] + 1
                length = i - subStrMap[s[i]] # Set by i - last appearance
                subStrMap[s[i]] = i #Update index with next appearance
                i += 1
            else: # Add char and record index, update max sub length if new max
                subStrMap[s[i]] = i
                length += 1
                if length > maxSubLength:
                    maxSubLength = length
                i += 1
        return maxSubLength

Sol = Solution()
print(Sol.lengthOfLongestSubstring("abcabcbb"))
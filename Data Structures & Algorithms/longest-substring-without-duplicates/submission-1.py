class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        tempString=""
        for c in s:
            if c in tempString:
                index=tempString.find(c)
                tempString=tempString[index+1:]
                
            tempString+=c
            longest=max(longest, len(tempString))
        
        return longest
class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for word in strs:
            counter=0
            for char in word:
                counter+=1
            string += str(counter)+"#"+word
        return string

    def decode(self, s: str) -> List[str]:
        left=0
        right=0
        strings=[]

        while right<len(s):
            while s[right]!='#':
                right+=1
            length=int(s[left:right])
            left=right+1
            right=left+length
            strings.append(s[left:right])
            left=right
        
        return strings




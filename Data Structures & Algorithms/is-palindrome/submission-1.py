class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=re.sub(r'[^a-z0-9]', '', s)
        count = -1;
        length = len(s)//2
        for i in range(length):
            if s[i] != s[count]:
                return False
            count -= 1
        
        return True



        
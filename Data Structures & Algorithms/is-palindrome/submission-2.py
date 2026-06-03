class Solution:
    def isPalindrome(self, s: str) -> bool:
        w = "".join(c for c in s if c.isalnum())
        word = w.lower()
        n = round(len(word)/2)
        r = 0
        for i in range(0, n):
            if word[i] == word[-i-1]:
                i+=1
                r = i
            else:
                break
        if r == n:
            return True
        else: 
            return False
            
                
            
    
        
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def ispalindromic(word):
            n = len(word)
            for i in range(n):
                if word[i]!=word[n-1-i]:
                    return False
            return True
        for word in words:
            if ispalindromic(word): return word
        return ''
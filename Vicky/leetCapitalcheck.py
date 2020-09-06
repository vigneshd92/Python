class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #if word.isupper(): return True 24ms/13.7 mb
        #if word.islower():return True
       # return (word[0].isupper() and word[1:].islower())

        if (word.isupper() or word.islower()) : return True
        return (word[0].isupper() and word[1:].islower())
        #24ms/13.8 mb

obj = Solution()
print(obj.detectCapitalUse("fdfA"))
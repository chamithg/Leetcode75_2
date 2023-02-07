class Solution:
    def longestPalindrome(self, words):
        
        
        map = {}
        length = 0
        for i in words:
            char_1 = i[0]
            char_2 = i[1]
            if char_1 == char_2 and i in map:
                length +=4
                del map[char_2+ char_1]
            elif char_2+ char_1  in map:
                length +=4
                del map[char_2+ char_1]
            else:
                map[i] =1
        return length
words = ["lc","cl","cl","lc"]
obj = Solution()
print(obj.longestPalindrome(words))
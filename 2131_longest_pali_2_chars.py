class Solution:
    
    
    #  partially working but more complex
    def longestPalindrome(self, words): 
        map = {}
        eq_chars = {}
        length = 0
        for i in words:
            char_1 = i[0]
            char_2 = i[1]
            if char_1 == char_2:
                if i in eq_chars:
                    eq_chars[i] += 1
                else:
                    eq_chars[i] = 1
            elif char_2+ char_1  in map:
                length +=4
                del map[char_2+ char_1]
            else:
                map[i] = 1
        for k, v in eq_chars.items():
            if v % 2 == 0:
                length += v*2
                eq_chars[k] = 0
            else:
                length += (v-1) *2
                eq_chars[k] = 1
        for k, v  in eq_chars.items():
            if v ==1:
                length += 2
                break
        print(eq_chars,map)
        return length
words = ["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"]
obj = Solution()
print(obj.longestPalindrome(words))
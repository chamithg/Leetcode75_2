class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        output = s
        if len(s)<len(t):return ""
        # if len(s)==len(t):
        #     if s == t:
        #         return s
        #     else:
        #         return ""
        if len(t) ==1:
            if t in s:
                return t
            else:
                return ""
        # function to create counter
        def Counter (s):
            counter ={}
            for i in s:
                if i not in counter:
                    counter[i] = 1
                else:
                    counter[i] +=1
            return counter
                    
        #  create t counter:
        t_count = Counter(t)
        #  crete helper function to match with t counter
        def match (s):
            for k,v in t_count.items():
                if k not in s or s[k] <v:
                    return False
            return True
        
        # initiate two windows 
        p1 = 0
        p2 = 0
        
        while p2<len(s):
            if match(Counter(s[p1:p2+1])):
                if len(output)> len(s[p1:p2+1]):
                    output = s[p1:p2+1]
                p1 +=1
                while p1<=p2 and s[p1] not in t_count:
                    p1 +=1
            else: p2+=1
                    
            
        
        return output



s = "ADOBECODEBANC"
t = "ABC"
obj = Solution()
print(obj.minWindow(s,t))
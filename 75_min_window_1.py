
class Solution:
    
    def minWindow(self, s: str, t: str) -> str:
        # function to create counter
        def Counter (s):
            counter ={}
            for i in s:
                if i not in counter:
                    counter[i] = 1
                else:
                    counter[i] +=1
            return counter
        output = ""
        if len(s)<len(t):return ""
        if len(s)==len(t):
            if Counter(s) == Counter(t):
                return s
            else:
                return ""
        if len(t) ==1:
            if t in s:
                return t
            else:
                return ""
        
                    
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
        
        s_count = Counter(s[p1:p2+1])
        
        while p2<len(s):
            
            if match(s_count):
                if len(output)> len(s[p1:p2+1]) or output =="":
                    output = s[p1:p2+1]
                s_count[s[p1]] -=1
                p1 +=1
            else:
                if p2 == len(s)-1: break
                p2+=1
                if s[p2] not in s_count:
                    s_count[s[p2]] =1
                else:
                    s_count[s[p2]] +=1
                        
        return output

   
        



s = "ADOBECODEBANC"
t = "ABC"
obj = Solution()
print(obj.minWindow(s,t))
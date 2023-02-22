
#  this works for most of scenarios
class Solution:
    def calculate(self, s: str) -> int:
        s_arr = []
        nums = ""
        for i in s:
            if i  == "+" or i  == "*" or i  == "/" or i  == "-":
                if nums != "":
                    s_arr.append(int(nums))
                    nums = ""
                s_arr.append(i)
            elif i ==" ":
                if nums != "":
                    s_arr.append(int(nums))
                    nums = ""
                continue
            else:
                nums+=i
        
        if nums !="":
            s_arr.append(int(nums))
            
        
        # devision
        i = 0
        while  i < (len(s_arr)):
            if s_arr[i] == "/":
                temp = s_arr[i-1]//s_arr[i+1]
                s_arr[i-1] = temp
                del s_arr[i]
                del s_arr[i]
            i+=1
        # multiplication
        i = 0
        while  i < (len(s_arr)):
            if s_arr[i] == "*":
                temp = s_arr[i-1] * s_arr[i+1]
                s_arr[i-1] = temp
                del s_arr[i]
                del s_arr[i]
            i+=1
        
        # addition
        i = 0
        while  i < (len(s_arr)):
            if s_arr[i] == "+":
                temp = s_arr[i-1] + s_arr[i+1]
                s_arr[i-1] = temp
                del s_arr[i]
                del s_arr[i]
            i+=1
        
        
        # substraction
        i = 0
        while  i < (len(s_arr)):
            if s_arr[i] == "-":
                temp = s_arr[i-1] - s_arr[i+1]
                s_arr[i-1] = temp
                del s_arr[i]
                del s_arr[i]
            i+=1
        return s_arr[0]

s = "3/2"
obj = Solution()
print(obj.calculate(s))
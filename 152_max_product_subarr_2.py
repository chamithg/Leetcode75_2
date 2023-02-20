class Solution:
    def maxProduct(self, nums):
        
        #  this solution works but too slow
        min_val = 1
        max_val = 1
        
        out_val = 1
        
        
        #  because we have negative values in the array, we need to keep track of posible max and min val
        # up to each index. the min val of the cur index could be the greater value at the next index 
        # (neg *  neg == positive)
        
        for n in nums:
            if n == 0: 
                min_val , max_val =1,1
                continue
            temp_min_val = min_val
            min_val = min(n * min_val, n* max_val,n)
            max_val = max(n * temp_min_val, n* max_val,n)
            out_val = max(min_val,max_val,out_val)
        
        return out_val

nums = [2,3,-2,4]
obj = Solution()
print(obj.maxProduct(nums))
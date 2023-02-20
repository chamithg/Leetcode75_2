class Solution:
    def maxProduct(self, nums):
        
        #  this solution works but too slow
        self.max_val = float('-inf')
        def find(ind,sum):
            if sum> self.max_val:
                self.max_val = sum
                if ind < len(nums):
                    find(ind+1, sum*nums[ind +1])
        
        for i in range(len(nums)):
            find(i,nums[i])
        
        return self.max_val

nums = [2,3,-2,4]
obj = Solution()
print(obj.maxProduct(nums))
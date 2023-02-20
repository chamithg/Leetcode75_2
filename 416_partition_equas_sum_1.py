class Solution:
    def canPartition(self, nums):
        
        total = 0
        for i in nums:
            total += i
        
        target = total/2
        
        found_sums = set()
        found_sums.add(0)
        for i in nums:
            temp = set()
            temp.add(i)
            for j in found_sums:                
                temp.add(i+j)
            found_sums.update(temp)
        return target in found_sums    
        




nums = [1,5,11,5]
obj = Solution()
print(obj.canPartition(nums))

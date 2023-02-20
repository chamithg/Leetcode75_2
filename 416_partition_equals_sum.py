class Solution:
    def canPartition(self, nums):
        
        #  this solution works but not efficient
        
        total = 0
        for i in nums:
            total += i
        
        target = total/2
        self.found = False
        # create a function to iterate over the nums untill find target
        def find(index,target):
            if nums[index] == target: 
                self.found = True
                return 
            # check the target with including current no
            else:
                if index<len(nums)-1 and nums[index +1] <= target :
                    find(index+1,target-nums[index])
                    # check the target excluding current no
                    find(index +1,target)
                else:return
        
        for i in range(len(nums)):
            find(i,target)
            return self.found



nums = [1,5,11,5]
obj = Solution()
print(obj.canPartition(nums))

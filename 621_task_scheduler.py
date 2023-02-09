class Solution:
    def leastInterval(self, tasks,n):
        if n == 0:
            return len(tasks)
        map = {}
        for task in tasks :
            if task not in map:
                map[task] =1
            else:
                map[task] +=1
        if len(map)> n:
            return len(tasks)
        time = 0
        while len(map) > 0:
            task_done = 0
            for k,v in map.items():
                map[k] -=1
                task_done +=1
                
            
            
        


tasks = ["A","A","A","B","B","B"]
n = 2
obj = Solution()
print(obj.leastInterval(tasks,n))
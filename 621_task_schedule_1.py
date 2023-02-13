class Solution:
    def leastInterval(self, tasks,n):
        if n == 0:
            return len(tasks)
        map = {}
        
        #  create the counter 
        for task in tasks :
            if task not in map:
                map[task] =1
            else:
                map[task] +=1
        # if n+1 <= len(map):
        #     return len(tasks)   
        longest_task_count = 0
        tasks_at_last_seq = 0
        
        for k, v in map.items():
            longest_task_count = max(longest_task_count,v)
        
        for k, v in map.items():
            if v == longest_task_count:
                tasks_at_last_seq +=1
        time = (longest_task_count-1)  * (n +1)
        print(time,tasks_at_last_seq)
        return  max(time + tasks_at_last_seq,len(tasks))
            


tasks = ["A","A","A","B","B","B","B"]
n = 5
obj = Solution()
print(obj.leastInterval(tasks,n))
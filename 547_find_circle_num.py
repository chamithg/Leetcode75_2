class Solution(object):
    def findCircleNum(self, M):
         # Step 1: Create a visited set to keep track of visited nodes
        visited = set()

        # Step 2: Traverse the nodes in the graph
        circles = 0
        for i in range(len(M)):
            if i not in visited:
                self.dfs(M, i, visited)
                circles += 1

        # Step 4: Return the total number of friend circles
        return circles

    def dfs(self, M, node, visited):
        visited.add(node)
        for i in range(len(M)):
            if M[node][i] == 1 and i not in visited:
                self.dfs(M, i, visited)
                
        
        
        
isConnected =[[1,1,0],[1,1,0],[0,0,1]]
obj = Solution()
print(obj.findCircleNum(isConnected))

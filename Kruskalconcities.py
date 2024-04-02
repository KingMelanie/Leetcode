class Solution(object):
   
    def find(self, x):
        if self.parent[x] == -1:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return
        self.parent[parent_y] = parent_x

    def minimumCost(self, n: int, connections :list[list[int]]) -> int:

        self.parent = [ -1 for i in range(n+1)]
        disjoint = n-1
        cost = 0
        c = sorted(connections,key=lambda v:v[2])
        i = 0
        while i<len(c) and disjoint:
            x = c[i][0]
            y = c[i][1]
            if self.find(x)!=self.find(y):
                disjoint-=1
                cost+=c[i][2]
                self.union(x,y)
                i+=1
        return cost if not disjoint else -1
    
ob1 = Solution()
print("Minimum cost of connecting cities is: ", ob1.minimumCost(3, [[1,2,5], [1,3,6], [2,3,1]]))
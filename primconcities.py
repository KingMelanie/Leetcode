from typing import List
import heapq
class Solution:
    def minimumCost(self, N: int, connections: list[list[int]]) -> int:
    # build graph
        graph = {}
        for i in range(1, N+1):
            graph[i] = []
        for x, y, cost in connections:
            graph[x].append((y, cost))
            graph[y].append((x, cost))
        
        pq = [(0, 1)]
        visited = set()
        total = 0
        while pq:
            cost, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            total += cost
            for neighbor, neighbor_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (neighbor_cost, neighbor))
        return total if len(visited) == N else -1
    
ob1 = Solution()
print("\nMinimum cost of connecting cities is: ", ob1.minimumCost(3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]))
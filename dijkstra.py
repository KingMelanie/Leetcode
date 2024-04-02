import heapq
import collections

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u,v,w in times:
            if u == v: return -1
            graph[u].append((v,w))
        if k not in graph: return -1
        
        pq = [(0,k)]
        dict ={}
        while pq:
            step, source = heapq.heappop(pq)
            if source in dict: continue
            dict[source]=step
            for target, distance in graph[source]:
                if target not in dict:
                    heapq.heappush(pq, (step+distance, target))
        return max(dict.values()) if len(dict) == n else -1
    
# case 1
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
#Output: 2

ob1 = Solution()
print("Leetcode's first case: ", ob1.networkDelayTime(times = 
    [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))

# case 2
#Input: times = [[1,2,1]], n = 2, k = 1
#Output: 1

ob1 = Solution()
print("Leetcode's second case: ", ob1.networkDelayTime(times = [[1,2,1]], n = 2, k = 1))

# case 3
#Input: times = [[1,2,1]], n = 2, k = 2
#Output: -1

ob1 = Solution()
print("Leetcode's third case: ", ob1.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))
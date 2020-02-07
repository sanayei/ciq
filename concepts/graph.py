# implementation of disjoint union find
# from https://leetcode.com/problems/redundant-connection/discuss/246972/Union-find-python-(general-approach)-beats-99
# Number of Islands II
# Couples Holding Hands
# Most Stones Removed
# Redundant Connection
class DSU:
    def __init__(self):
        self.parents = {}

    def make_set(self, x):
        self.parents[x] = x

    def find(self, x):
        if x not in self.parents:
            self.parents[x] = x
            return self.parents[x]
        elif self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        else:
            self.parents[root_x] = root_y
            return True


# shortest path
# There are N network nodes, labelled 1 to N.
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
# Now, we send a signal from a certain node src. How long will it take for all nodes to receive the signal? If it is impossible, return -1
# times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, src = 2
def shortestpath(times, N, src):
    from collections import defaultdict
    import heapq
    graph = defaultdict(dict)
    for u, v, w in times:
        graph[u][v] = w
    heap = [(0, src)]
    seen = {}
    while heap:
        distance, node = heapq.heappop(heap)
        if node not in seen:
            seen[node] = distance
            for nei in graph[node]:
                heapq.heappush(heap, (distance+graph[node][nei], nei))
    if len(seen) == N:
        return max(seen.values())
    else:
        return -1



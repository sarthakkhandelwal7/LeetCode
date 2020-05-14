from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


class Solution:

    def criticalConnections(self, n: int, connections):
        network = Graph()

        for n1, n2 in connections:
            network.add_edge(n1, n2)

        visited = [False] * n
        curr_val = [float('inf')] * n
        lowest_val = [float('inf')] * n
        parent = [-1] * n
        ans = []

        def dfs(u):
            visited[u] = True
            curr_val[u] = network.time
            lowest_val[u] = network.time
            network.time += 1

            for v in network.graph[u]:
                if not visited[v]:
                    parent[v] = u
                    dfs(v)

                    lowest_val[u] = min(lowest_val[u], lowest_val[v])
                    if curr_val[u] < lowest_val[v]:
                        ans.append([u, v])

                elif parent[u] != v:
                    lowest_val[u] = min(lowest_val[u], curr_val[v])

        for u in network.graph.keys():
            if not visited[u]:
                dfs(u)

        return ans

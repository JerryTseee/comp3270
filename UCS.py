from heapq import heappush, heappop

def UCS(graph, start, goal):
    frontier = []
    heappush(frontier, (0, start))
    explored_set = set()
    while frontier:
        node = heappop(frontier)
        if node[1].endswith(goal):
            return node
        if node[1][-1] not in explored_set:
            explored_set.add(node[1][-1])
            for i in graph[node[1][-1]]:
                heappush(frontier, (node[0]+i[0], node[1] + i[1]))
                
graph = {
    'A': [(1, 'B'), (2, 'C')],
    'B': [(3, 'D')],
    'C': [(4, 'D')],
    'D': [(5, 'E')],
    'E': []
}

print(UCS(graph, 'A', 'E'))
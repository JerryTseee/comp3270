from heapq import heappush, heappop

def aStarTSA(graph, h, start, goal):
    frontier = []
    heappush(frontier, (h[start], start))
    while frontier:
        node = heappop(frontier)
        if node[1].endswith(goal):
            return node
        else:
            for child in graph[node[1][-1]]:
                heappush(frontier, (node[0]+child[0]-h[node[1][-1]]+h[child[1]], node[1] + child[1]))

aStarMotivation = {
'S':[(1,'a')],'a':[(1,'b'),(3,'d'),(8,'e')],'b':[(1,'c')],'c':[],'d':[(2,'G')],'e':[(1,'d')]}
aStarMotivationH = {'S':6,'a':5,'b':6,'c':7,'d':2,'e':1,'G':0}
print('Solution path:',aStarTSA(aStarMotivation, aStarMotivationH, 'S', 'G'))
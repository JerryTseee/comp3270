from heapq import heappush, heappop

def greedyTSA(graph, h, start, goal):
    frontier = []
    heappush(frontier, (h[start], start))
    while frontier:
        node = heappop(frontier)
        if node[1].endswith(goal):
            return node
        else:
            for i in graph[node[1][-1]]:
                heappush(frontier, (h[i[1]], node[1] + i[1]))
                
romania = {
'A':[(140,'S'),(118,'T'),(75,'Z')],'Z':[(75,'A'),(71,'O')],'O':[(151,'S'),(71,'Z')],
'T':[(118,'A'),(111,'L')],'L':[(70,'M'),(111,'T')],'M':[(75,'D'),(70,'L')],
'D':[(120,'C'),(75,'M')],'S':[(140,'A'),(99,'F'),(151,'O'),(80,'R')],
'R':[(146,'C'),(97,'P'),(80,'S')],'C':[(120,'D'),(138,'P'),(146,'R')],
'F':[(211,'B'),(99,'S')],'P':[(101,'B'),(138,'C'),(97,'R')],'B':[]
}
romaniaH = {
'A':366,'B':0,'C':160,'D':242,'E':161,'F':176,'G':77,'H':151,'I':226,
'L':244,'M':241,'N':234,'O':380,'P':100,'R':193,'S':253,'T':329,'U':80,
'V':199,'Z':374}
print('Solution path:',greedyTSA(romania, romaniaH, 'A', 'B'))
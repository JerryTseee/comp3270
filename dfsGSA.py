import collections

def dfsGSA(stateSpaceGraph, start, goal):
    frontier = collections.deque([start])
    explored_set = set()

    while frontier:
        node = frontier.pop()
        if node.endswith(goal): return node
        if node[-1] not in explored_set:
            explored_set.add(node[-1])
            for i in stateSpaceGraph[node[-1]]:
                frontier.append(node + i)

stateSpaceGraph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

startState = 'A'
goalState = 'D'

# Call the bfsTSA function to find a path from startState to goalState
result = dfsGSA(stateSpaceGraph, startState, goalState)

if result:
    print(f"Path from {startState} to {goalState}: {result}")
else:
    print("No path found from the start state to the goal state.")
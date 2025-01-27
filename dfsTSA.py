import collections

def dfsTSA(graph, start, goal):
    frontier = collections.deque([start])
    while frontier:
        node = frontier.pop()
        if node.endswith(goal): return node
        for i in graph[node[-1]]:
            frontier.append(node + i)

# Define a simple state space graph as an adjacency list
stateSpaceGraph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

startState = 'A'
goalState = 'D'

# Call the bfsTSA function to find a path from startState to goalState
result = dfsTSA(stateSpaceGraph, startState, goalState)

if result:
    print(f"Path from {startState} to {goalState}: {result}")
else:
    print("No path found from the start state to the goal state.")
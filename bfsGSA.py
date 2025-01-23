import collections

def bfsGSA(stateSpaceGraph, startstate, goalstate):
    frontier = collections.deque([startstate])
    explored = set()
    while frontier:
        node = frontier.popleft()
        if node.endswith(goalstate):
            return node
        else:
            if node[-1] not in explored:
                explored.add(node[-1])
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
result = bfsGSA(stateSpaceGraph, startState, goalState)

if result:
    print(f"Path from {startState} to {goalState}: {result}")
else:
    print("No path found from the start state to the goal state.")
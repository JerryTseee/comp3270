import collections

def bfsTSA(stateSpaceGraph, startState, goalState):
    froniter = collections.deque([startState])
    while froniter:
        curr_node = froniter.popleft()
        if (curr_node.endswith(goalState)):
            return curr_node
        else:
            for child in stateSpaceGraph[curr_node[-1]]:
                froniter.append(curr_node + child)

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
result = bfsTSA(stateSpaceGraph, startState, goalState)

if result:
    print(f"Path from {startState} to {goalState}: {result}")
else:
    print("No path found from the start state to the goal state.")
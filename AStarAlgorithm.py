graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 5), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)],
    'G': []
}

heuristic = {'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0}
start = 'S'
goal = 'G'

def astar(graph, heuristic, start, goal):
    openlist = [(start, 0)]  # (node, g-cost)
    path = {start: [start]}
    visited = {}

    while openlist:
        # Select node with minimum f = g + h
        openlist.sort(key=lambda x: x[1] + heuristic[x[0]])  # Sort based on f-cost
        current, g = openlist.pop(0)

        if current == goal:
            return path[current]  # Return path if goal is reached

        if current in visited and visited[current] <= g:
            continue  # Skip if already visited with lower cost

        visited[current] = g  # Mark node as visited

        for neighbor, cost in graph[current]:
            new_g = g + cost
            if neighbor not in visited or new_g < visited[neighbor]:  # Check for better path
                openlist.append((neighbor, new_g))
                path[neighbor] = path[current] + [neighbor]  # Store the path

    return None  # No path found

# Run A* Search
path = astar(graph, heuristic, start, goal)
if path:
    print("-->".join(path))
else:
    print("NO PATH FOUND")

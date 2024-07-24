
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)


graph = {'A': set(['B', 'C','D']),
         'B': set(['E']),
         'C': set(['D','E']),
         'D': set([]),
         'E': set([])}

dfs(graph, 'A')
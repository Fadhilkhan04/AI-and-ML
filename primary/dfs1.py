graph = {
  'A' : ['B','C','D'],
  'B' : ['E'],
  'C' : ['D','E'],
  'D' : [],
  'E' : [],
  
}

visited = []
stack = []  

def dfs(visited, graph, node): 
  visited.append(node)
  stack.append(node)
  
  while stack:   
    m = stack.pop() 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        stack.append(neighbour)


print("Following is the Breadth-First Search")
dfs(visited, graph, 'A')  
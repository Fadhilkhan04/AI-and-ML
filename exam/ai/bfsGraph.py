graph = {
  '1':['4','6','2'],
  '2':[],
  '3':['2','5'],
  '4':['7'],
  '5':[],
  '6':[],
  '7':['3']
}

visited = []
queue = []

def bfs(visited,graph,node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)
    print(m,end=" ")

    for i in graph[m]:
      if i not in visited:
        visited.append(i)
        queue.append(i)

print("bfs is:")
bfs(visited,graph,'1')
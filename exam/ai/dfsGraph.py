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
stack = []

def dfs(visited,graph,node):
  visited.append(node)
  stack.append(node)

  while stack:
    m = stack.pop()
    print (m, end = " ") 

    for i in graph[m]:
      if i not in visited:
        visited.append(i)
        stack.append(i)

print("the dfs is :")
dfs(visited,graph,'1')
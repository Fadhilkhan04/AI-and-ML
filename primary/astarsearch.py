from queue import PriorityQueue

class Node:
    def _init_(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def _eq_(self, other):
        return self.position == other.position

    def _lt_(self, other):
        return self.f < other.f

def astar_search(start, goal, grid):
    open_list = PriorityQueue()
    closed_list = set()
    
    start_node = Node(start)
    goal_node = Node(goal)
    
    open_list.put((0, start_node))
    
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    while not open_list.empty():
        current_node = open_list.get()[1]
        closed_list.add(current_node.position)
        
        if current_node == goal_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        children = []
        for direction in directions:
            new_position = (current_node.position[0] + direction[0],
                            current_node.position[1] + direction[1])
            
            if 0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0]):
                if grid[new_position[0]][new_position[1]] == 0:
                    new_node = Node(new_position, current_node)
                    children.append(new_node)
        
        for child in children:
            if child.position in closed_list:
                continue
            
            child.g = current_node.g + 1
            child.h = abs(child.position[0] - goal_node.position[0]) + abs(child.position[1] - goal_node.position[1])
            child.f = child.g + child.h
            
            in_open_list = False
            for open_node in open_list.queue:
                if child == open_node[1] and child.g >= open_node[1].g:
                    in_open_list = True
                    break
            if not in_open_list:
                open_list.put((child.f, child))

    return None

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar_search(start, goal, grid)

if path:
    print(f"Path found: {path}")
else:
    print("No path found")
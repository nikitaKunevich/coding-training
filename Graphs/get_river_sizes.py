'''
Given matrix of rivers (1's) and lands(0's) return array of all river lengths.
e.g. for matrix:
[
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]
answer would be: [1,2,2,2,5]
'''

# O(w*h) time | O(w*h) space
def riverSizes(area):
    n = len(area)
    if n == 0:
        return []
    m = len(area[0])
    if m == 0:
        return []
    rivers = []
    visited = [[False for _ in range(m)] for _ in range(n)]

    for out_i in range(n):
        for out_j in range(m):
            if visited[out_i][out_j]:
                continue
            traverse_node(out_i,out_j,area,visited,rivers,n,m)
    return rivers
    
def traverse_node(out_i,out_j,area,visited,rivers,n,m):
    walk_stack = [(out_i,out_j)]
    river = 0
    while walk_stack:
        row,col = walk_stack.pop()
        if row < 0 or row >= n or col < 0 or col >=m:
            continue
        if visited[row][col]:
            continue
        visited[row][col] = True
        
        if area[row][col] == 0:
            continue
            
        river+=1
        for n_i,n_j in get_unvisited_neighbours(row,col,area,visited,n,m):
            walk_stack.append((n_i,n_j))
    if river > 0:
        rivers.append(river)
        
def get_unvisited_neighbours(i,j,area,visited,n,m):
    neighbours = []
    if i > 0 and not visited[i-1][j]:
        neighbours.append((i-1,j))
    if i < n - 1 and not visited[i+1][j]:
        neighbours.append((i+1,j))
    if j > 0 and not visited[i][j-1]:
        neighbours.append((i,j-1))
    if j < m - 1 and not visited[i][j+1]:
        neighbours.append((i,j+1))
    return neighbours

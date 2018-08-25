# ret: 返回连通区域个数，最大连通区域大小

def dfs(graph, x, y):
    graph[x][y] = 0
    ret = 1
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx; ny = y + dy
            if (0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 1):
                ret += dfs(graph, nx, ny)
    return ret

graph = [
    [ 0, 1, 1, 0, 0 ],
    [ 0, 0, 1, 1, 0 ],
    [ 0, 1, 1, 1, 0 ],
    [ 1, 0, 0, 0, 0 ],
    [ 0, 0, 1, 1, 0 ]
]

R, C = len(graph), len(graph[0])

res = 0
maxr = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == 1:

            maxr = max(maxr, dfs(graph, i, j))

            res += 1

print (res, maxr)
